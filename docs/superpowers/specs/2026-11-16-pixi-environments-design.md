# Pixi Environments for Dataset and Training CLIs

## Goal

Provide reproducible, explicitly selected Pixi environments for local development, Molab, and RunPod while keeping the dataset and training CLI dependency sets separate.

## Context

Issue #9 asks to simplify development because the repository contains separate dependency sets. The repository currently has three project manifests:

- `corpus_builder/pyproject.toml` defines `satyrn-corpus-builder`, Python `>=3.13`, and the `satyrn-dataset` command.
- `trainer/unsloth/pyproject.toml` defines `satyrn-unsloth`, Python `>=3.13.9,<3.14`, and the `satyrn-unsloth` command.
- `spikes/pep750/pyproject.toml` defines a Python `>=3.14` experiment and is not part of the production dataset/training workflow.

The dataset CLI exposes `cpt`, `sft`, `rl`, `download-inputs`, and `collect-doc-changes`. Its entrypoint imports and registers all command modules at startup, so a dataset environment needs the dataset package's complete runtime dependency set. The trainer CLI imports its training, tracking, and evaluation stack, including Unsloth, PyTorch, Transformers, TRL, Hugging Face Datasets, Hydra, MLflow, and Inspect.

Training versions are not one-size-fits-all. The trainer documentation calls for `trl==1.7.0`; Mellum 2 was tested with `transformers==5.15.0`, while Gemma 4 uses `transformers==5.5.0`. Both use `torch==2.11.0` and `torchvision==0.26.0`, while the appropriate CUDA wheel source depends on the machine/driver. The current development host reports Linux x86_64, Python 3.12.3, and no `nvidia-smi`; it is below both CLI packages' Python floors and has no detected NVIDIA GPU. The repository's reported Molab setup uses Python 3.13.11 and a CUDA 13.2 driver. RunPod's operating-system, Python, driver, and CUDA constraints have not yet been recorded. Confirm whether the current host is the intended local target before treating its hardware facts as universal.

Pixi supports both `pixi.toml` and `pyproject.toml` manifests, PyPI dependencies through uv, multiple named environments, and platform-specific lock resolution. This supports the requirement for target-specific environments while preserving the existing Python package projects.

## Design

### Package and environment boundaries

Create a repository-root `pixi.toml` and `pixi.lock` to manage environments; do not replace the two package manifests. Keep `corpus_builder/pyproject.toml` and `trainer/unsloth/pyproject.toml` as the sources of package metadata, runtime dependencies, and console entry points.

Every named environment must include exactly one CLI package: either `satyrn-corpus-builder` or `satyrn-unsloth`, never both. This prevents the two packages' conflicting requirements from being forced into the same environment. Use Pixi features to share common setup and compose target-specific dependencies, but define named environments for the supported workflows so users select them explicitly.

At minimum, define a dataset environment and separate training environments for local, Molab, and RunPod. Model-specific training selections (Mellum and Gemma) must remain separate whenever their Transformers requirements differ. Add dataset environments per deployment target only if inventory shows those targets need different dataset dependencies or Python versions.

Keep `spikes/pep750` outside these CLI environments. Its Python `>=3.14` requirement is incompatible with the trainer's `<3.14` bound, and it is an experiment rather than a production CLI package.

### Target inventory and Python policy

Before finalizing platform pins, record for local, Molab, and RunPod:

- operating system and architecture;
- Python version available to the job;
- GPU model and NVIDIA driver version, if a GPU is used;
- required CUDA wheel source/runtime;
- which CLI and model profiles the target must run.

The trainer package requires Python `>=3.13.9,<3.14`; Molab's recorded Python 3.13.11 fits. The dataset package independently allows Python `>=3.13`. Keep these constraints in the package metadata and select compatible Python versions per Pixi environment rather than imposing a workspace-wide Python intersection. Do not claim support for a target platform until its environment resolves and the relevant CLI starts there.

### Dependency and lock policy

Use Pixi's PyPI dependency support for the existing Python packages and retain the current package dependency declarations. Use Conda packages only for system/native dependencies that are needed and available from the selected channels; do not install the same library through both Conda and PyPI in one environment.

Keep the following training requirements explicit:

- `trl==1.7.0`;
- Mellum: `transformers==5.15.0`;
- Gemma: `transformers==5.5.0`;
- `torch==2.11.0` and `torchvision==0.26.0`;
- PyPI's Torch 2.11 CUDA 13.0 (`cu130`) wheel path and the explicit PyTorch CUDA 12.8 (`cu128`) index where the target driver requires it.

Pixi does not remove upstream dependency metadata conflicts by itself. Prototype the Unsloth bounds against the desired TRL/Transformers profiles before choosing a supported PyPI override or metadata strategy. Do not globally force one Transformers version, upgrade Unsloth, or silently change model behavior. Keep the environment profiles and resulting lock resolution inspectable and reproducible.

### User workflow and documentation

Document the equivalent of package-scoped operations through named Pixi environments. The final environment names must reflect the verified target inventory; examples should follow this shape:

```sh
# Dataset-only environment
pixi install -e dataset
pixi run -e dataset satyrn-dataset --help
pixi run -e dataset satyrn-dataset cpt --help

# A training environment for a specific target and model profile
pixi install -e molab-gemma
pixi run -e molab-gemma satyrn-unsloth --help

# Run a configured experiment after selecting the matching model environment
pixi run -e molab-gemma satyrn-unsloth --config-name experiment/py3.15
```

The trainer guide must explain how to choose the target environment, model profile, and CUDA wheel source. The dataset guide must show that its environment does not install the trainer's GPU stack. The README must link new users to these workflows.

### CI

Update CI to install Pixi and use the lockfile. Run dataset tests in the dataset environment and trainer tests in a documented trainer profile so CI never combines the two CLI dependency sets. Preserve the existing Ruff checks and test coverage. Do not add a new type-checking job or broaden the CI matrix beyond the environments needed to validate this change.

## Success Criteria

1. `pixi.lock` resolves the selected platforms and environments, and a lock check succeeds without modifying the lock.
2. The dataset environment installs and runs `satyrn-dataset` without installing the trainer package or GPU stack.
3. Each selected trainer environment installs and starts `satyrn-unsloth` without installing the dataset package.
4. Local, Molab, and RunPod environment definitions use Python and CUDA choices verified for those targets; unknown target values are not guessed.
5. The Mellum and Gemma Transformers selections both resolve in separate environments and remain explicitly documented.
6. The `cu128` source is selected only for targets that require it; the default PyPI `cu130` path remains explicit.
7. CI uses Pixi environments and the lockfile while existing lint and test jobs pass.
8. A new contributor can install and run either CLI by selecting its environment, without manually installing packages with pip.

## Risks and Constraints

- Local and RunPod target details are not present in the repository; they must be obtained before those environments can be pinned.
- Unsloth's declared bounds conflict with the issue comments' working TRL/Transformers versions. Pixi's PyPI resolution must be tested for a transparent, reproducible override strategy.
- GPU wheel compatibility depends on host drivers and platform support. A successful lock is not proof of runtime CUDA compatibility.
- Dataset and trainer environments must stay separate; adding both CLI packages to one environment would reintroduce the dependency conflict this design is meant to avoid.
- Pixi's PyPI and Conda dependencies must not install duplicate versions of Torch, CUDA libraries, or other native packages into one environment.

## Out of Scope

- Adding `spikes/pep750` to production CLI environments.
- Upgrading Unsloth or changing model-training behavior.
- Adding a new type checker or broad CI redesign.
- Replacing the existing dataset or training CLIs.
