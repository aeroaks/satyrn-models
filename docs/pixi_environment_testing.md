# Testing the Pixi environments locally and on Molab

This guide lists the commands for continuing validation of the repository's [Pixi](https://pixi.sh) environments.
Environment definitions live in `pixi.toml`; the target and model-profile notes are in
[trainer_unsloth.md](trainer_unsloth.md).

Each named environment installs one CLI package, so dataset generation and model training use separate environments.

## Prerequisites

- Install Pixi by following the [official Pixi installation documentation](https://pixi.sh/latest/installation/).
  The repository lock (`pixi.lock`) was generated with Pixi 0.84.1. Use `pixi --version` to check yours.
- Install and run commands use `--locked`, so they fail instead of silently updating `pixi.lock`.
- For the optional full train/evaluation run only: `HF_TOKEN`, `HF_USERNAME`, `MLFLOW_TRACKING_USERNAME` and
  `MLFLOW_TRACKING_PASSWORD` (the trainer's `load_secrets()` asserts all four), the dataset files used by the
  experiment config, enough GPU memory and permission to download the model. See [trainer_molab.md](trainer_molab.md)
  for how to provide credentials in a `.env` file. Never put tokens directly into commands.

## What has and has not been verified

| Target | Verified | Not verified |
|---|---|---|
| Local host (Linux x86_64, Python 3.12.3, no `nvidia-smi`) | `dataset-local` provides its own Python 3.13.x and the dataset CLI | Trainer GPU training: not supported on this host |
| Molab (Linux x86_64, Python 3.13.11, NVIDIA RTX PRO 6000 Blackwell Server Edition, driver 595.71.05; operator-verified) | Host details only | Actual CUDA wheel source, trainer CLI startup and model-profile runtime support |

The `molab-*` environments are **candidate** profiles, not verified Molab support:

- `molab-mellum` and `molab-gemma` were import- and CLI-help-checked on a CPU-only host, not on Molab.
- `molab-qwen36-35b` is lock-only: building `causal-conv1d` failed locally without CUDA.
- `molab-qwen36-27b` is an unverified candidate; its Torch 2.11, TRL 1.7 and mslk 1.1.1 overrides are not recorded by the model config.
- PyPI Torch 2.11 currently resolves to `2.11.0+cu130` in the candidate Mellum and Gemma environments. That has not been
  verified on Molab, and there is no Pixi cu128 feature yet.
- There is no RunPod environment. RunPod target details have not been supplied, so no RunPod install command or support is documented.

## Local: dataset CLI and tests

```sh
# Dataset CLI
pixi install --locked -e dataset-local
pixi run --locked -e dataset-local python -V
pixi run --locked -e dataset-local satyrn-dataset --help

# Dataset tests
pixi install --locked -e dataset-ci
pixi run --locked -e dataset-ci pytest -q corpus_builder/tests
```

`python -V` should report the environment's own Python 3.13.x, not the host's Python.

## Local: trainer tests (pytest)

> [!NOTE]
> `trainer-ci` uses the Gemma profile, so installing it pulls the full Gemma/Torch/NVIDIA dependency stack
> (multiple GB) even on a host without a GPU. The tests themselves do not need a GPU.

```sh
pixi install --locked -e trainer-ci
pixi run --locked -e trainer-ci pytest -q trainer/unsloth/tests
```

> [!WARNING]
> `trainer/unsloth/tests/test_datasets.py::test_packed_sequences_fit_seq_len` downloads a public Hugging Face
> tokenizer. It fails on a host behind a TLS-intercepting proxy such as Cisco Umbrella (the observed local host). Do not
> disable certificate checks. Run that test in trusted CI or on a network with a normal Hugging Face TLS chain.

## Molab: inspect versions and CUDA without training

Run these in the Molab terminal (or through a `run(...)` helper as in [trainer_molab.md](trainer_molab.md)) from the
repository root, on a GPU-enabled notebook.

```sh
# Gemma candidate: inspect versions and CUDA without starting training
pixi install --locked -e molab-gemma
pixi run --locked -e molab-gemma python -c "import sys, torch, transformers, trl; print(sys.version.split()[0], transformers.__version__, torch.__version__, trl.__version__, torch.version.cuda, torch.cuda.is_available())"
pixi run --locked -e molab-gemma satyrn-unsloth --help

# Mellum candidate
pixi install --locked -e molab-mellum
pixi run --locked -e molab-mellum satyrn-unsloth --help
```

Record the output. This is a GPU preflight only: `torch.cuda.is_available()` printing `True` is necessary but does not
establish runtime support. Reserve "runtime verified" for a successful training and evaluation run on the target. The CLI
help alone is not evidence of GPU runtime support either.

## Molab: optional full train/evaluation run

> [!CAUTION]
> This is **not** a quick smoke test. It is a full, potentially expensive end-to-end run: `experiment/py3.15` enables
> both CPT and SFT, and the trainer evaluates the model after every selected stage. `pre_model_eval=false` skips only the
> evaluation before training; `max_steps=1` does not skip the post-stage evaluations.

Prerequisites:

- `HF_TOKEN`, `HF_USERNAME`, `MLFLOW_TRACKING_USERNAME` and `MLFLOW_TRACKING_PASSWORD` in `.env` (`load_secrets()` asserts all four).
- The dataset files named in the config, fetched through Git LFS.
- Enough GPU memory and the Gemma 4 model download.
- The evaluation interpreters from the next section (Python 3.13, 3.14 and 3.15 through uv).

```sh
pixi run --locked -e molab-gemma satyrn-unsloth --config-name experiment/py3.15 model=gemma-4-26B-A4B-it max_steps=1 pre_model_eval=false
```

A successful run would be the first runtime evidence for the Gemma candidate on Molab. Until then it stays unverified.

## Python interpreters for evaluation: uv as a runtime helper

Pixi manages the package and CLI environments. However, the trainer's version-specific evaluation still finds its
subprocess interpreters by running `uv python find` (`code_tester.find_interpreter()` in
`trainer/unsloth/src/satyrn/trainer/unsloth/rl/code_tester.py`), and it needs Python 3.13, 3.14 and 3.15 for
target and predecessor versions. Pixi global Python installs do not satisfy that code path, so uv remains a runtime
helper until the code is refactored. Install it as a Pixi global tool and let it install the interpreters:

```sh
pixi global install uv
uv --version
uv python install 3.13 3.14 3.15
```

Pixi exposes global tools in `~/.pixi/bin`; make sure that directory is on `PATH`. In a Molab notebook, add it to the
environment used by the `run()` helper before invoking uv:

```py
import os
from pathlib import Path

os.environ["PATH"] = str(Path.home() / ".pixi" / "bin") + os.pathsep + os.environ["PATH"]
```

These interpreters are only for the trainer's evaluator; they do not replace the Pixi application environment. This is
the only current use of uv in these docs; do not use `uv pip` or `uv sync` to install packages.
