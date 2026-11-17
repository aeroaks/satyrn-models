# Model training on Molab notebooks

This tutorial explains how to run the training experiments on the Molab notebooks with the repository's Pixi environments.

> [!WARNING]
> The `molab-*` Pixi environments are candidate profiles. Molab runtime support is not verified: the CUDA wheel source, trainer
> CLI startup and model-profile support still need to be checked on Molab. Follow
> [pixi_environment_testing.md](pixi_environment_testing.md) to check the versions and CUDA before training. The
> older Qwen 3.8 / uv instructions are kept only as [legacy material](trainer_tutorial.md).

## Pre-requisites

- Create an account on <https://molab.marimo.io/>
- Generate the Hugging Face token (`HF_TOKEN`, plus your `HF_USERNAME`)
- Request the MLflow account on discord. Training needs it: the trainer requires `MLFLOW_TRACKING_USERNAME` and
  `MLFLOW_TRACKING_PASSWORD` along with the Hugging Face values and fails at startup without all four.
- (Only for a private fork) Generate a GitHub API token. The upstream repository is public and needs none to clone.
- [Pixi](https://pixi.sh/latest/installation/) available in the notebook's terminal (check with `pixi --version`; install it following the official documentation if missing)

## Notebook preparation

First things first, open a new notebook in Molab.

Then, copy all your keys to the `.env.example` and upload that as `.env` to Molab notebook filesystem.

## Environment setup

In a "Configure Resources" dropdown in the top panel, choose the GPU accelerator. At the moment (in the free trier) only the 'RTX Pro 6000' is available.

In a new cell put the following imports and a function. The function echoes every command it runs, so never put
tokens or passwords into command strings.

```py
import marimo as mo
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(".env")

# Pixi's global tools (such as uv, installed below) live in ~/.pixi/bin
os.environ["PATH"] = str(Path.home() / ".pixi" / "bin") + os.pathsep + os.environ["PATH"]

import subprocess

def run(cmd, **kwargs):
    print(f"$ {cmd}")
    result = subprocess.run(cmd, shell=True, env=os.environ, **kwargs)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed ({result.returncode}): {cmd}")
    return result
```

Then, call the following set of commands:

```py
run("apt update && apt install -y git-lfs")
run("git lfs install")
run("rm -rf satyrn-models")
run("git clone --branch issue-9-uv-workspaces https://github.com/aeroaks/satyrn-models.git")
run("cd satyrn-models && pixi install --locked -e molab-gemma")
```

Pixi manages the package and CLI environments. The trainer's version-specific evaluation, however, still discovers
its Python 3.13, 3.14 and 3.15 subprocess interpreters by running `uv python find`
(`code_tester.find_interpreter()`), until that code is refactored. Pixi global Python installs do not satisfy that code path,
so install uv as a Pixi global tool and let it install the interpreters. These interpreters are only for the
evaluator; they do not replace the Pixi application environment.

```py
run("pixi global install uv")
run("uv --version")
run("uv python install 3.13 3.14 3.15")
```

Candidate environments are named `molab-<profile>`; see the [environment table](trainer_unsloth.md#install) for the
available profiles (`molab-mellum`, `molab-gemma`, `molab-qwen36-27b`, `molab-qwen36-35b`). Choose one environment for
the model you want to train. `molab-gemma` is used below as an example.

## GPU preflight

Inspect the environment and CUDA before training:

```py
run("""
cd satyrn-models && pixi run --locked -e molab-gemma python -c "import sys, torch, transformers, trl; print(sys.version.split()[0], transformers.__version__, torch.__version__, trl.__version__, torch.version.cuda, torch.cuda.is_available())"
""")
run("cd satyrn-models && pixi run --locked -e molab-gemma satyrn-unsloth --help")
```

This is a GPU preflight only. `torch.cuda.is_available()` being `True` is necessary, but not sufficient; a profile is
runtime verified only after a successful training and evaluation run on Molab.

## Optional full train/evaluation run (Gemma candidate)

> [!CAUTION]
> This is a full, potentially expensive end-to-end run, not a quick smoke test. `experiment/py3.15` enables both CPT and
> SFT, and the trainer evaluates the model after every selected stage. `pre_model_eval=false` skips only the evaluation
> before training; `max_steps=1` does not skip the post-stage evaluations.

Prerequisites: all four credentials (`HF_TOKEN`, `HF_USERNAME`, `MLFLOW_TRACKING_USERNAME`,
`MLFLOW_TRACKING_PASSWORD`) in `.env`, the dataset files named in the config (fetched through Git LFS), enough GPU
memory, the Gemma 4 model download, and the evaluation interpreters installed above. The command is an unverified candidate:

```py
run("""
cd satyrn-models && pixi run --locked -e molab-gemma satyrn-unsloth --config-name experiment/py3.15 model=gemma-4-26B-A4B-it max_steps=1 pre_model_eval=false
""")
```

For the full set of local and Molab checks, see [pixi_environment_testing.md](pixi_environment_testing.md).

## Extras

Note that Molab files manipulation UI is quite tricky. You may then want to clone your own fork instead:

```py
run("git clone https://github.com/<your-gh-login>/satyrn-models.git")
```

A private fork needs a GitHub token; configure Git credentials (for example the GitHub CLI's `gh auth login`) in the Molab terminal rather than putting the token into a command or URL, because `run()` echoes commands.

Work on a branch of the fork with a new config. Alternatively, you can also edit the files via the Molab terminal,
which you can open by toggling the developer panel at the very left bottom.
