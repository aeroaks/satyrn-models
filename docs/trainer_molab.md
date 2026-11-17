# Model training on Molab notebooks

This tutorial explains how to run the training experiments on the Molab notebooks with the repository's Pixi environments.

> [!WARNING]
> The `molab-*` Pixi environments are candidate profiles. Molab runtime support is not verified: the CUDA wheel source, trainer
> CLI startup and model-profile support still need to be checked on Molab. Follow
> [pixi_environment_testing.md](pixi_environment_testing.md) to check the versions and CUDA before training. The
> older Qwen 3.8 / uv instructions are kept only as [legacy material](trainer_tutorial.md).

## Pre-requisites

- Create an account on https://molab.marimo.io/
- Generate the Github API token
- Generate the Hugging Face token
- (Optional) Request on discord the mlflow account
- [Pixi](https://pixi.sh/latest/installation/) available in the notebook's terminal (check with `pixi --version`; install it following the official documentation if missing)

## Notebook preparation

First things first, open a new notebook in Molab.

Then, copy all your keys to the `.env.example` and upload that as `.env` to Molab notebook filesystem.

## Training launch

In a "Configure Resources" dropdown in the top panel, choose the GPU accelerator. At the moment (in the free trier) only the 'RTX Pro 6000' is available.

In a new cell put the following imports and a function:

```py
import marimo as mo
import os
from dotenv import load_dotenv

load_dotenv(".env") 

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
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
run(f"git clone https://${GITHUB_TOKEN}@github.com/satyrn-ai/satyrn-models.git")
run("cd satyrn-models && pixi install --locked -e molab-gemma")
run("pixi global install --environment satyrn-eval-py314 --expose python3.14=python python=3.14")
run("pixi global install --environment satyrn-eval-py315 --expose python3.15=python python=3.15")
```

The global Python 3.14 and 3.15 interpreters are used by the evaluation subprocesses; the trainer itself runs in the
selected Pixi environment. Make sure Pixi's global bin directory is on `PATH` so `python3.14` and `python3.15` are found.

Candidate environments are named `molab-<profile>`; see the [environment table](trainer_unsloth.md#install) for the
available profiles (`molab-mellum`, `molab-gemma`, `molab-qwen36-27b`, `molab-qwen36-35b`). Choose one environment for
the model you want to train. `molab-gemma` is used below as an example.

Before training, inspect the environment and CUDA:

```py
run("""
cd satyrn-models && pixi run -e molab-gemma python -c "import sys, torch, transformers, trl; print(sys.version.split()[0], transformers.__version__, torch.__version__, trl.__version__, torch.version.cuda, torch.cuda.is_available())"
""")
run("cd satyrn-models && pixi run -e molab-gemma satyrn-unsloth --help")
```

Continue only if `torch.cuda.is_available()` is `True`. The `.env` credentials are loaded into the notebook
environment by `load_dotenv`, so do not paste them into commands.

## Optional one-step smoke test (Gemma candidate)

This downloads the Gemma 4 model and starts training, so it can be slow and costly. Credentials, dataset files and
enough GPU memory are prerequisites. It is an unverified candidate command:

```py
run("""
cd satyrn-models && pixi run -e molab-gemma satyrn-unsloth --config-name experiment/py3.15 model=gemma-4-26B-A4B-it max_steps=1 pre_model_eval=false
""")
```

For the full set of local and Molab checks, see [pixi_environment_testing.md](pixi_environment_testing.md).

## Extras

Note that Molab files manipulation UI is quite tricky. You may then want to clone your own fork instead:

```py
run(f"git clone https://${GITHUB_TOKEN}@github.com/<your-gh-login>/satyrn-models.git")
```

and work of the branch with a new config. Alternatively, you can also edit the files via the Molab terminal,
which you can open by toggling the developer panel at the very left bottom.
