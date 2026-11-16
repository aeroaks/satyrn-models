# Model training

Use the `satyrn-unsloth` package to fine-tune models with Unsloth.

## Target environments

A target is supported only after its package environment resolves and the CLI starts there. "Reported" values come from repository or issue comments and were not re-verified; "not recorded" means no verified value is available.

| Target | Platform | Python | GPU/driver | CLI | Model profiles |
|---|---|---|---|---|---|
| Local development host | Linux x86_64 (observed) | 3.12.3 (observed); below both CLI floors (`satyrn-dataset` `>=3.13`, `satyrn-unsloth` `>=3.13.9,<3.14`) | No `nvidia-smi` observed; no GPU training target | Dataset CLI development only, once a Python `>=3.13` environment is available; trainer CLI not supported (no GPU observed) | None for training |
| Molab | Not recorded in this session | 3.13.11 (reported; fits `satyrn-unsloth`) | CUDA 13.2 driver (reported); GPU model and CUDA wheel source not recorded | Trainer CLI (`satyrn-unsloth`); dataset CLI not recorded | Not recorded; not verified |
| RunPod | Not recorded | Not recorded | Not recorded; CUDA 12.8 or 13.0 wheel source not determined | Not recorded | Not recorded; not verified |

Model profile requirements recorded in `trainer/unsloth/configs/model`:

- Mellum 2 (`mellum2-12b-a2.5`): `transformers==5.15.0`.
- Gemma 4 (`gemma-4-26B-A4B-it`): `transformers==5.5.0`.
- Qwen 3.6 (`qwen3.6-27b`, `qwen3.6-35b-a3b`): `transformers==5.3.0`; the 35B config also lists `trl 0.22.2` and `torch 2.8.0`, which conflict with this guide's `torch==2.11.0`.
- Qwen 2.5 0.5B, Qwen 3 Coder 30B-A3B, Qwen 3.8 27B, and Ornith 1.5 9B: no Transformers version recorded in their configs.

## Install

Prerequisites:
- make sure you have a Python version matching `>=3.13.9,<3.14`

Install the `satyrn-unsloth` command into your environment from the `trainer/unsloth` package.

```sh
uv pip install -e ./trainer/unsloth
```

Unsloth installs `trl==0.24.0` which has a known bug [trl#6105](https://github.com/huggingface/trl/issues/6105).
We need to upgrade `trl`:

```sh
uv pip install "trl==1.7.0"
```

### Transformers version

**Note:** Different `transformers` versions are required for different models.

For Mellum 2 we need `transformers>=5.10.1`. Tested on `5.15.0`, install it using:

```sh
uv pip install "transformers==5.15.0" "torch==2.11.0" "torchvision==0.26.0"
```

Gemma 4 does not work with `transformers==5.15.0`, stick with the Unsloth-shipped version:

```sh
uv pip install "transformers==5.5.0" "torch==2.11.0" "torchvision==0.26.0"
```

### CUDA build

PyPI `torch==2.11.0` is a CUDA 13 build (`+cu130`). If using older 570-series Nvidia drivers and CUDA 12.8, you will need a build from `pytorch.org` instead:

```sh
uv pip install "torch==2.11.0" "torchvision==0.26.0" \
  --extra-index-url https://download.pytorch.org/whl/cu128
```

## Run a fine-tuning experiment

Pass the name of an experiment config to `satyrn-unsloth`.

```sh
satyrn-unsloth --config-name experiment/pep750-qwen2.5-0.5b
```

In experiment config `py3.15` you can swap the model with `model=`, naming any config in 
`trainer/unsloth/configs/model`:

```sh
satyrn-unsloth --config-name experiment/py3.15 model=qwen3.6-27b
```

Anything set in the experiment config can be overridden on the same line:

```sh
satyrn-unsloth --config-name experiment/py3.15 model=qwen3-coder-30b-a3b load_in_4bit=true cpt.batch_size=2
```
