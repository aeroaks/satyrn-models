# Testing the Pixi environments locally and on Molab

This guide lists the commands for continuing validation of the repository's [Pixi](https://pixi.sh) environments.
Environment definitions live in `pixi.toml`; the target and model-profile notes are in
[trainer_unsloth.md](trainer_unsloth.md).

Each named environment installs one CLI package, so dataset generation and model training use separate environments.

## Prerequisites

- Install Pixi by following the [official Pixi installation documentation](https://pixi.sh/latest/installation/).
  The repository lock (`pixi.lock`) was generated with Pixi 0.84.1. Use `pixi --version` to check yours.
- Commands use `--locked`, so they fail instead of silently updating `pixi.lock`.
- For the Molab smoke test only: a Hugging Face token, the dataset files used by the experiment config, enough GPU
  memory and permission to download the model. See [trainer_molab.md](trainer_molab.md) for how to provide credentials in a `.env`
  file. Never put tokens directly into commands.

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
pixi run -e dataset-local python -V
pixi run -e dataset-local satyrn-dataset --help

# Dataset tests
pixi install --locked -e dataset-ci
pixi run -e dataset-ci pytest -q corpus_builder/tests
```

`python -V` should report the environment's own Python 3.13.x, not the host's Python.

## Local: trainer tests

```sh
pixi install --locked -e trainer-ci
pixi run -e trainer-ci pytest -q trainer/unsloth/tests
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
pixi run -e molab-gemma python -c "import sys, torch, transformers, trl; print(sys.version.split()[0], transformers.__version__, torch.__version__, trl.__version__, torch.version.cuda, torch.cuda.is_available())"
pixi run -e molab-gemma satyrn-unsloth --help

# Mellum candidate
pixi install --locked -e molab-mellum
pixi run -e molab-mellum satyrn-unsloth --help
```

Record the output. Call a profile runtime-verified only after you have inspected the Python, Torch and CUDA values and
`torch.cuda.is_available()` prints `True`. The CLI help alone is not evidence of GPU runtime support.

## Molab: optional one-step Gemma smoke test

> [!CAUTION]
> This is optional and potentially costly: it downloads the Gemma 4 model and starts training. Run it only after the
> checks above pass. Credentials, dataset files, sufficient GPU memory and the model download are prerequisites.

```sh
pixi run -e molab-gemma satyrn-unsloth --config-name experiment/py3.15 model=gemma-4-26B-A4B-it max_steps=1 pre_model_eval=false
```

A successful run would be the first runtime evidence for the Gemma candidate on Molab. Until then it stays unverified.

## Python 3.14 and 3.15 for evaluation subprocesses

Evaluation runs generated code in subprocesses and needs Python 3.14 and 3.15 interpreters. These are separate from
the project CLI environment, which uses the Python selected by its Pixi environment. Install the evaluation interpreters
as Pixi global environments:

```sh
pixi global install --environment satyrn-eval-py314 --expose python3.14=python python=3.14
pixi global install --environment satyrn-eval-py315 --expose python3.15=python python=3.15
```

Pixi exposes `python3.14` and `python3.15` in its global bin directory; make sure that directory is on `PATH`
(`pixi global list` shows the installed environments). Check with `python3.14 -V` and `python3.15 -V`.
