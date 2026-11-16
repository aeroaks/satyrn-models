# Model training

Use the `satyrn-unsloth` package to fine-tune models with Unsloth.

## Target environments

A target is supported only after its package environment resolves and the CLI starts there; no target is supported yet. "Operator-verified" values were supplied by the operator from command output. "Reported" values come from repository or issue comments and were not re-verified. "Not recorded" means no verified value is available.

| Target | Platform | Python | GPU/driver | CLI | Model profiles |
|---|---|---|---|---|---|
| Local development host | Linux x86_64 (observed) | 3.12.3 (observed); below both CLI floors (`satyrn-dataset` `>=3.13`, `satyrn-unsloth` `>=3.13.9,<3.14`) | No `nvidia-smi` observed; no GPU training target | Dataset CLI development only, through the `dataset-local` Pixi environment, which provides its own Python 3.13 and the CLI (host Python 3.12.3 is not used); trainer CLI not supported (no GPU observed) | None for training |
| Molab | Linux x86_64 (operator-verified) | 3.13.11 (operator-verified; fits `satyrn-unsloth`) | NVIDIA RTX PRO 6000 Blackwell Server Edition, driver 595.71.05 (operator-verified); CUDA 13.2 driver previously reported, not re-verified; CUDA wheel source not provided | Trainer CLI (`satyrn-unsloth`) intended, not verified; dataset CLI not recorded | Not verified; environment resolution and CLI startup not tested |
| RunPod | Not recorded | Not recorded | Not recorded; CUDA 12.8 or 13.0 wheel source not determined | Not recorded | Not recorded; not verified |

Model profile requirements recorded in `trainer/unsloth/configs/model`. None of these stacks is verified as a Pixi environment yet; the `molab-*` Pixi environments below are candidate locks only.

- Mellum 2 (`mellum2-12b-a2.5`): tested with `transformers==5.15.0`; the minimum is `transformers>=5.10.1`. 5.15.0 is the tested version, not a universal requirement.
- Gemma 4 (`gemma-4-26B-A4B-it`): `transformers==5.5.0`; the guide notes 5.15.0 does not work with it.
- Qwen 3.6 (not verified):
  - `qwen3.6-27b`: `transformers 5.3.0`, plus flash-linear-attention and causal_conv1d; no TRL or Torch version recorded. The `molab-qwen36-27b` environment uses Torch 2.11.0, TRL 1.7.0 and mslk 1.1.1 as candidate environment choices inherited from `uv.toml`; they are not model-recorded pins and are unverified.
  - `qwen3.6-35b-a3b`: the only Qwen 3.6 profile with a recorded Torch/TRL stack, a separate stack from the Torch 2.11 profiles in the Install section below: `transformers 5.3.0`, `trl 0.22.2`, and `torch 2.8.0`, plus flash-linear-attention and causal_conv1d 1.6.0, which builds only against torch 2.8.0.
- Qwen 3.8 27B shares the Qwen3.6 27B hybrid-attention (Fast Linear Attention) dependency pattern: `flash-linear-attention` and `causal_conv1d`, with a torch fallback when they are missing. It has no dedicated Pixi environment and no tested environment.
- Qwen 2.5 0.5B, Qwen 3 Coder 30B-A3B, and Ornith 1.5 9B: no Transformers version recorded in their configs.

## Install

Prerequisites:
- [Pixi](https://pixi.sh)
- an NVIDIA GPU host for training (the local development host has no GPU and cannot run the trainer)

Environments are managed with Pixi. Each named environment intentionally installs one CLI package: either the
dataset package or the training package, never both. `satyrn-unsloth` environments also pin one target and
one model profile, so choose a separate environment for each target/model combination. Do not combine the dataset
and trainer features to build one universal environment. For dataset generation, use `dataset-local` as described
in [dataset_generator.md](dataset_generator.md).

| Environment | Target | Model profile | Pinned stack | Status |
|---|---|---|---|---|
| `molab-mellum` | Molab | Mellum 2 / 2.1 | Python 3.13.11, Transformers 5.15.0 (minimum `>=5.10.1`), TRL 1.7.0, Torch 2.11.0, torchvision 0.26.0 | Candidate lock; Molab support not verified |
| `molab-gemma` | Molab | Gemma 4 | Python 3.13.11, Transformers 5.5.0, TRL 1.7.0, Torch 2.11.0, torchvision 0.26.0 | Candidate lock; Molab support not verified |
| `molab-qwen36-27b` | Molab | Qwen 3.6 27B | Python 3.13.11, Transformers 5.3.0, Torch 2.11.0, flash-linear-attention, causal-conv1d; TRL 1.7.0 and mslk 1.1.1 are unverified candidate settings | Candidate lock; not verified on any target |
| `molab-qwen36-35b` | Molab | Qwen 3.6 35B-A3B | Python 3.13.11, Transformers 5.3.0, TRL 0.22.2, Torch 2.8.0, flash-linear-attention, causal-conv1d 1.6.0 | Lock only; building causal-conv1d failed on the local no-CUDA host |

There is no RunPod environment: RunPod details are not recorded. There is no Qwen 3.8 27B environment; see the
profile notes above.

The `molab-*` environments are candidate locks: they record what resolves, not verified Molab support. The CUDA
wheel source, model requirements, and actual CLI startup on Molab are not verified. Treat the trainer examples
below as candidate and unverified.

Install an environment, then run the CLI inside it:

```sh
# Gemma 4 on Molab (candidate, unverified)
pixi install -e molab-gemma
pixi run -e molab-gemma satyrn-unsloth --help
```

Mellum 2 needs a different `transformers` version than Gemma 4 (5.15.0 versus 5.5.0; Gemma 4 does not work with
5.15.0), so it has its own environment:

```sh
# Mellum 2.1 on Molab (candidate, unverified)
pixi install -e molab-mellum
pixi run -e molab-mellum satyrn-unsloth --help
```

Unsloth pins `trl==0.24.0`, which has a known bug [trl#6105](https://github.com/huggingface/trl/issues/6105),
and caps `transformers` at 5.5.0. The Pixi environments override these pins; the overrides live in `pixi.toml`.

### CUDA build

PyPI `torch==2.11.0` is a CUDA 13 build (`+cu130`). If using older 570-series Nvidia drivers and CUDA 12.8, you need a
build from `pytorch.org` instead. Pixi CUDA 12.8 configuration is pending target evidence: no target is confirmed
to need it, so there is no Pixi cu128 environment yet.

The `molab-mellum` and `molab-gemma` candidate environments currently resolve Torch from PyPI (`2.11.0+cu130`). That
is a candidate configuration, not verified Molab support: the Molab CUDA wheel source is not confirmed. The Torch 2.8.0
source for `molab-qwen36-35b` is also unverified.

## Run a fine-tuning experiment

Run `satyrn-unsloth` with `pixi run -e <environment>`, using the environment that matches your target and model.
Pass the name of an experiment config. The examples below are candidate and unverified on Molab.

For Mellum, use its experiment config in the `molab-mellum` environment:

```sh
pixi run -e molab-mellum satyrn-unsloth --config-name experiment/py3.15-mellum2.1-12b-a2.5b
```

In experiment config `py3.15` you can swap the model with `model=`, naming any config in
`trainer/unsloth/configs/model`. It defaults to `qwen2.5-0.5b`, for which no Pixi environment exists, so override
`model=` to match your environment:

```sh
pixi run -e molab-gemma satyrn-unsloth --config-name experiment/py3.15 model=gemma-4-26B-A4B-it
```

Anything set in the experiment config can be overridden on the same line. Only use a model whose requirements
match the selected environment:

```sh
pixi run -e molab-gemma satyrn-unsloth --config-name experiment/py3.15 model=gemma-4-26B-A4B-it load_in_4bit=true cpt.batch_size=2
```
