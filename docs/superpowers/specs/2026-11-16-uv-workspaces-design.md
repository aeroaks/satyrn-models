# uv Workspace for Dataset and Training CLIs

## Goal

Provide a reproducible uv workspace for developing and running the dataset-builder and Unsloth-training CLIs locally and on Molab, while keeping their dependency choices and operational commands explicit.

## Context

Issue #9 asks to simplify development to `uv sync` because the repository contains separate dependency sets. The repository currently has three project manifests:

- `corpus_builder/pyproject.toml` defines `satyrn-corpus-builder`, Python `>=3.13`, and the `satyrn-dataset` command.
- `trainer/unsloth/pyproject.toml` defines `satyrn-unsloth`, Python `>=3.13.9,<3.14`, and the `satyrn-unsloth` command.
- `spikes/pep750/pyproject.toml` defines a Python `>=3.14` experiment and is not part of the production dataset/training workflow.

The dataset CLI exposes `cpt`, `sft`, `rl`, `download-inputs`, and `collect-doc-changes`. Its entrypoint imports and registers all command modules at startup, so a dataset-only environment still needs the dataset package's complete runtime dependency set. The trainer CLI imports its training, tracking, and evaluation stack, including Unsloth, PyTorch, Transformers, TRL, Hugging Face Datasets, Hydra, MLflow, and Inspect.

Training versions are not one-size-fits-all. The trainer documentation calls for `trl==1.7.0`; Mellum 2 was tested with `transformers==5.15.0`, while Gemma 4 uses `transformers==5.5.0`. Both use Torch 2.11 and torchvision 0.26, while the appropriate CUDA wheel source depends on the machine/driver. Molab's reported working environment uses Python 3.13.11 and CUDA 13.2.

## Design

### Workspace boundary and Python policy

Create a repository-root uv workspace containing only `corpus_builder` and `trainer/unsloth`. Keep `spikes/pep750` outside the workspace: its Python `>=3.14` requirement is incompatible with the trainer's `<3.14` bound, and it is an experiment rather than a production CLI package.

The workspace Python range must reflect the intersection required by its members: `>=3.13.9,<3.14`. Developers on both local machines and Molab should use a Python version in that range. The workspace root will be a non-package coordinator; the existing member projects remain the installable packages and retain their own dependency declarations.

### Dependency and lockfile policy

Use one repository-root `uv.lock` to resolve the two workspace members together. Keep package-specific runtime and development dependencies in their respective `pyproject.toml` files. Audit direct imports in the trainer package and declare libraries used directly by its code rather than relying on incidental transitive dependencies.

Do not impose one global Transformers version: the documented Mellum and Gemma workflows require different versions. Represent model-specific versions and CUDA wheel-source choices as explicit training profiles or documented, reproducible environment selections. Use uv resolver overrides only for verified metadata conflicts, and validate that an override needed for TRL does not invalidate either model workflow. Do not silently rewrite upstream package metadata or upgrade Unsloth as part of this issue.

### Explicit user workflows

The documentation will show package-scoped operations for normal work and a full-workspace operation for users who intentionally need both packages installed:

```sh
# Dataset development and command discovery
uv sync --package satyrn-corpus-builder
uv run --package satyrn-corpus-builder satyrn-dataset --help
uv run --package satyrn-corpus-builder satyrn-dataset cpt --help

# Training development and command discovery
uv sync --package satyrn-unsloth
uv run --package satyrn-unsloth satyrn-unsloth --help
uv run --package satyrn-unsloth satyrn-unsloth --config-name experiment/py3.15

# Install all workspace packages when both environments are wanted
uv sync --all-packages
```

The training guide will retain explicit model and hardware guidance. It will show how the selected training profile relates to the required Transformers version and how to select the appropriate PyTorch wheel source for the local or Molab driver environment. Dataset generation will not require installing the trainer's GPU stack when the user selects the dataset package only.

### CI and documentation

Update CI to use the workspace lock and uv-managed package installation instead of independently installing both editable projects with `uv pip`. Preserve the existing Ruff checks and test coverage. If Ruff is run as a uv tool, pin its existing version (`0.16.2`) explicitly. Do not add a new type-checking job or change the project's test scope as part of this issue.

Update the dataset and training guides to replace hand-managed installation steps with the package-scoped workspace examples above, while preserving required API-key, Docker, model, and CUDA prerequisites.

## Success Criteria

1. `uv lock --check` succeeds from the repository root with both production packages in one workspace lock.
2. A Python version satisfying `>=3.13.9,<3.14` can sync and run the dataset CLI without installing the trainer package when using the package-scoped dataset workflow.
3. The trainer package can be synced and its CLI launched through uv on the documented local and Molab setups.
4. The Mellum and Gemma Transformers selections both resolve and remain explicitly documented; a change for one does not silently change the other.
5. The documented CUDA wheel selection remains usable for the supported Molab and local driver cases.
6. CI uses the root lock consistently and the existing lint and test jobs pass.
7. A new contributor can follow the docs to choose dataset-only, trainer-only, or all-package setup without manually installing packages with pip.

## Risks and Constraints

- uv workspaces share a Python constraint and lockfile. The common Python range therefore excludes Python 3.14 even though the dataset package alone permits it.
- The trainer's GPU dependencies are large and platform-sensitive. A full-workspace sync is intentionally distinct from the lightweight package-scoped dataset sync.
- The trainer currently relies on some libraries that are imported by source but arrive transitively. Making these direct dependencies explicit may expose additional resolver conflicts.
- Unsloth's declared bounds conflict with the issue comments' working TRL/Transformers versions. Any resolver override must be checked against both model profiles and both local and Molab environments.
- A lockfile alone cannot guarantee that a CUDA wheel is compatible with every local driver; the docs must retain the explicit wheel-source selection.

## Out of Scope

- Adding `spikes/pep750` to the workspace.
- Upgrading Unsloth or changing model-training behavior.
- Adding a new type checker or broad CI redesign.
- Replacing the existing dataset or training CLIs.
