# Pixi Environment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add reproducible Pixi environments for local, Molab, and RunPod use while keeping the dataset and training CLI dependency sets isolated.

**Architecture:** Keep `corpus_builder` and `trainer/unsloth` as separate Python packages. Add a root Pixi workspace with features and named environments; every environment contains exactly one CLI package, and target/model features select the appropriate Python, PyTorch source, and Transformers version. Keep environment profiles separate when dependency versions conflict.

**Tech Stack:** Pixi (`pixi.toml`, `pixi.lock`, features, environments, tasks), existing PEP 621 package metadata, PyPI packages resolved by Pixi, GitHub Actions, pytest, Ruff.

**Spec:** `docs/superpowers/specs/2026-11-16-pixi-environments-design.md`

## Global Constraints

- Keep `corpus_builder` and `trainer/unsloth` as separate CLI packages; no named environment may include both.
- Dataset package requires Python `>=3.13`; trainer requires `>=3.13.9,<3.14`.
- The current local host is Linux x86_64 with Python 3.12.3 and no `nvidia-smi`; Pixi must provide a supported Python, and local GPU training must not be claimed without a verified GPU setup.
- Molab's reported baseline is Python 3.13.11 with a CUDA 13.2 driver; verify this before finalizing its lock profile.
- RunPod OS/architecture, Python, driver, and CUDA details are not yet recorded; collect them before pinning the RunPod profile.
- Keep `trl==1.7.0`, Torch `2.11.0`, and torchvision `0.26.0` explicit.
- Keep Mellum on `transformers==5.15.0` and Gemma on `transformers==5.5.0`, in separate environments.
- PyPI's Torch 2.11 wheel is the CUDA 13.0 path; use the explicit PyTorch CUDA 12.8 index only for targets that require it.
- Do not upgrade Unsloth, change model-training behavior, add a type-checking job, or add `spikes/pep750` to production CLI environments.

---

## File Structure

- `pixi.toml` — new root environment manifest: supported platforms, package-specific features, target/model profiles, tasks, and named environments.
- `pixi.lock` — generated lock for the declared platform and environment combinations.
- `corpus_builder/pyproject.toml` — retain dataset metadata and dependencies; add directly imported `docutils` if absent.
- `trainer/unsloth/pyproject.toml` — retain trainer metadata and declare runtime packages imported directly by trainer code.
- `.github/workflows/ci.yml` — install Pixi and run existing lint/test suites in isolated environments.
- `README.md`, `docs/dataset_generator.md`, `docs/trainer_unsloth.md` — setup matrix and copyable Pixi environment commands.

## Task 1: Capture target environment requirements

**Files:**
- Modify: `docs/trainer_unsloth.md`
- Verify: local, Molab, and RunPod runtime details

**Interfaces:**
- Produces a target matrix used to select Pixi platforms, Python versions, CUDA sources, and supported model profiles.
- A target is not listed as supported until its package environment resolves and the CLI starts there.

- [ ] **Step 1: Record the current local host facts**

Run:

```sh
python3 --version
uname -sm
if command -v nvidia-smi >/dev/null 2>&1; then nvidia-smi --query-gpu=name,driver_version --format=csv,noheader; else echo "nvidia-smi unavailable"; fi
```

The current development host has already reported Python `3.12.3`, Linux x86_64, and no `nvidia-smi`. Keep that fact in the matrix; it is below both CLI packages' Python floors and does not establish a local GPU-training target.

- [ ] **Step 2: Collect the same facts from Molab and RunPod**

Run the same three commands in each environment. Molab has a previously reported Python `3.13.11` and CUDA 13.2 driver; verify the current environment. Record RunPod's actual values rather than copying Molab's settings. If the agent cannot enter either target, ask the operator to provide the command output before creating its locked environment.

- [ ] **Step 3: Confirm which CLI/model combinations each target must support**

Use the target facts and the existing model configs to record whether each target needs the dataset CLI, trainer CLI, Mellum, Gemma, and CUDA 12.8. For the local host, distinguish dataset/development use from actual GPU training; do not promise local training on the observed no-GPU host.

- [ ] **Step 4: Add the verified environment matrix to the trainer guide**

Add a table to `docs/trainer_unsloth.md` with columns `Target`, `Platform`, `Python`, `GPU/driver`, `CLI`, and `Model profiles`. Include the observed local values and verified Molab/RunPod values. Do not list a missing or unverified value as supported.

- [ ] **Step 5: Commit the environment inventory**

```sh
git add docs/trainer_unsloth.md
git commit -m "docs: record Pixi target environments"
```

## Task 2: Add Pixi package features and isolated environments

**Files:**
- Create: `pixi.toml`
- Create: `pixi.lock` (generated)
- Modify: `corpus_builder/pyproject.toml`
- Modify: `trainer/unsloth/pyproject.toml`

**Interfaces:**
- `dataset` feature installs only the editable corpus-builder package.
- `trainer` feature installs only the editable Unsloth package.
- `mellum` and `gemma` are mutually exclusive environment features.
- Target-specific features select only verified platform/Python/CUDA differences from Task 1.

- [ ] **Step 1: Declare direct Python imports in the package manifests**

Add `docutils` to `[project].dependencies` in `corpus_builder/pyproject.toml`; `collect_doc_changes.py` imports it directly. Add directly imported `datasets`, `torch==2.11.0`, `torchvision==0.26.0`, `transformers`, and `trl==1.7.0` to `[project].dependencies` in `trainer/unsloth/pyproject.toml`. Keep existing Unsloth, Hydra, MLflow, Inspect, and other constraints unchanged. Do not add a single global Transformers pin to the trainer package.

- [ ] **Step 2: Create a Pixi root manifest with separate package features**

Create `pixi.toml` with the verified workspace platforms from Task 1 and this package-feature structure:

```toml
[workspace]
name = "satyrn-models"
channels = ["conda-forge"]
platforms = ["linux-64"]

[feature.dataset.dependencies]
python = ">=3.13"

[feature.dataset.pypi-dependencies]
satyrn-corpus-builder = { path = "corpus_builder", editable = true }

[feature.trainer.dependencies]
python = ">=3.13.9,<3.14"

[feature.trainer.pypi-dependencies]
satyrn-unsloth = { path = "trainer/unsloth", editable = true }
```

Use `platforms = ["linux-64"]` for the currently observed local host and the expected Linux GPU targets; add another platform only if Task 1 confirms a target that requires it. Define named environments by composing features, and never compose `dataset` and `trainer` in the same environment.

- [ ] **Step 3: Add model and target features from the verified matrix**

Add separate PyPI features for the documented model versions:

```toml
[feature.mellum.pypi-dependencies]
transformers = "==5.15.0"

[feature.gemma.pypi-dependencies]
transformers = "==5.5.0"
```

Create one named environment for each verified target/model combination, such as `molab-gemma` with `features = ["trainer", "molab", "gemma"]`. Define a `molab` or `runpod` feature only for dependencies that differ from the base trainer feature. If local training is not supported on the observed host, define `dataset-local` and a local trainer development environment only if the import/CLI smoke test succeeds; do not describe it as a training environment.

- [ ] **Step 4: Add target-specific PyTorch sources without mixing package managers**

For targets that require CUDA 12.8, define a dedicated Pixi feature that pins `torch==2.11.0` and `torchvision==0.26.0` and configures Pixi's feature-scoped PyPI index to `https://download.pytorch.org/whl/cu128`. Keep the default PyPI CUDA 13.0 source for Molab or other targets whose verified driver supports it. Confirm the generated lock records the selected index for the CUDA 12.8 environment. Do not install Torch or CUDA libraries from both Conda and PyPI in one environment.

- [ ] **Step 5: Resolve the Unsloth metadata conflicts in a Pixi prototype**

Run `pixi lock` with the editable trainer package and the separate `mellum` and `gemma` environments. Verify that Pixi resolves the Unsloth constraints together with `trl==1.7.0` and each Transformers pin without combining the two model profiles. If resolution fails, use only a Pixi-supported, environment-scoped PyPI override and rerun the lock. If Pixi cannot express the needed override without changing upstream metadata or merging the model environments, stop and ask before changing dependency policy or upgrading Unsloth.

- [ ] **Step 6: Install and smoke-test each isolated environment**

Run the following checks, substituting only a model/target environment that is actually declared in `pixi.toml`:

```sh
pixi install -e dataset-local
pixi run -e dataset-local satyrn-dataset --help
pixi install -e molab-gemma
pixi run -e molab-gemma python -c "import transformers; assert transformers.__version__ == '5.5.0'"
pixi list -e dataset-local
pixi list -e molab-gemma
```

Assert `5.15.0` in the declared Mellum environment. Repeat `pixi list -e` for each declared environment and confirm none contains both `satyrn-corpus-builder` and `satyrn-unsloth`.

- [ ] **Step 7: Commit the Pixi environments and package metadata**

```sh
git add pixi.toml pixi.lock corpus_builder/pyproject.toml trainer/unsloth/pyproject.toml
git commit -m "build: add isolated Pixi CLI environments"
```

## Task 3: Add new-user Pixi examples and target guidance

**Files:**
- Modify: `README.md`
- Modify: `docs/dataset_generator.md`
- Modify: `docs/trainer_unsloth.md`

**Interfaces:**
- New users select an environment with `pixi install -e <name>` and run commands with `pixi run -e <name>`.
- Dataset and trainer examples use different environments.
- Trainer examples state the selected deployment target, model profile, and CUDA source.

- [ ] **Step 1: Add a short Pixi quickstart to `README.md`**

Add this dataset-only example before the existing documentation links:

```sh
pixi install -e dataset-local
pixi run -e dataset-local satyrn-dataset --help
```

Link to the dataset and trainer guides for target-specific instructions.

- [ ] **Step 2: Replace dataset pip instructions with its named environment**

In `docs/dataset_generator.md`, replace the manual virtualenv and pip installation section with:

```sh
pixi install -e dataset-local
pixi run -e dataset-local satyrn-dataset --help
pixi run -e dataset-local satyrn-dataset cpt --help
```

Keep the API-key, Docker, input, and dataset-generation instructions unchanged.

- [ ] **Step 3: Document separate target/model training environments**

In `docs/trainer_unsloth.md`, document the environment matrix from Task 1 and replace manual pip pins with examples using verified names, such as:

```sh
pixi install -e molab-gemma
pixi run -e molab-gemma satyrn-unsloth --help
pixi run -e molab-gemma satyrn-unsloth --config-name experiment/py3.15
```

Add a separate Mellum example using its `transformers==5.15.0` environment. Add a CUDA 12.8 example only if Task 1 identifies a target that needs it. Preserve secrets, model, Docker, and training prerequisites.

- [ ] **Step 4: Explain Pixi environment selection**

Explain that Pixi's named environments intentionally install either the dataset package or the training package, and that users choose a separate environment for each target/model combination. Do not tell users to combine both CLI features to get one universal environment.

- [ ] **Step 5: Commit Pixi usage documentation**

```sh
git add README.md docs/dataset_generator.md docs/trainer_unsloth.md
git commit -m "docs: explain Pixi environment workflows"
```

## Task 4: Run CI in isolated Pixi environments

**Files:**
- Modify: `.github/workflows/ci.yml`
- Modify: `pixi.toml`

**Interfaces:**
- Lint uses a small Ruff-only Pixi environment.
- Dataset and trainer tests run in separate Pixi environments.
- CI installs from `pixi.lock` without silently updating it.

- [ ] **Step 1: Add lint and test tasks to `pixi.toml`**

Add a `lint` feature containing Ruff `0.16.2` and a `test` feature containing pytest `>=9,<10`. Define `dataset-ci` from `dataset` plus `test`, `trainer-ci` from `trainer`, one selected supported model profile, and `test`, and `lint` from only the lint feature. Keep `dataset-ci`, `trainer-ci`, and `lint` in separate solve groups unless they share the exact same resolved package set.

- [ ] **Step 2: Install Pixi in both CI jobs**

Add `prefix-dev/setup-pixi@v0.11.3` to the lint and test jobs in `.github/workflows/ci.yml`. Keep Git LFS checkout and current Linux x86_64 CI runner.

- [ ] **Step 3: Replace lint commands with the Pixi lint environment**

Replace the pipx Ruff install and direct Ruff invocations with:

```sh
pixi install --locked -e lint
pixi run -e lint ruff check trainer corpus_builder
pixi run -e lint ruff format --check trainer corpus_builder
```

- [ ] **Step 4: Run package tests in separate environments**

Replace the combined editable pip installation with:

```sh
pixi install --locked -e dataset-ci
pixi run -e dataset-ci pytest -v corpus_builder/tests
pixi install --locked -e trainer-ci
pixi run -e trainer-ci pytest -v trainer/unsloth/tests
```

Keep both test suites in CI and do not install both CLI packages into one Pixi environment.

- [ ] **Step 5: Commit CI migration**

```sh
git add .github/workflows/ci.yml pixi.toml pixi.lock
git commit -m "ci: use isolated Pixi environments"
```

## Task 5: Validate local, Molab, and RunPod workflows

**Files:**
- Test: `corpus_builder/tests/`
- Test: `trainer/unsloth/tests/`
- Verify: `pixi.toml`, `pixi.lock`, and the setup guides

- [ ] **Step 1: Verify the local dataset environment**

Run:

```sh
pixi install --locked -e dataset-local
pixi run -e dataset-local satyrn-dataset --help
pixi run -e dataset-local satyrn-dataset cpt --help
```

Expected: all commands succeed using Pixi's supported Python; the environment contains the dataset CLI and not the trainer package.

- [ ] **Step 2: Verify every configured model/target environment**

In each target, run the locked install and version checks for every environment actually listed in the target matrix. For example, run `pixi install --locked -e dataset-local`, `pixi install --locked -e molab-gemma`, and `pixi install --locked -e runpod-gemma` when those profiles are declared. For Mellum, verify Transformers `5.15.0`; for Gemma, verify `5.5.0`; verify Torch and torchvision are `2.11.0` and `0.26.0`; verify the CUDA 12.8 environment uses the PyTorch CUDA 12.8 index. On Molab and RunPod, run the training CLI's `--help` and a documented lightweight smoke run if credentials and hardware are available. Do not count lock resolution alone as proof that GPU training works.

- [ ] **Step 3: Run the CI-equivalent suites**

Run:

```sh
pixi install --locked -e lint
pixi run -e lint ruff check trainer corpus_builder
pixi run -e lint ruff format --check trainer corpus_builder
pixi install --locked -e dataset-ci
pixi run -e dataset-ci pytest -q corpus_builder/tests
pixi install --locked -e trainer-ci
pixi run -e trainer-ci pytest -q trainer/unsloth/tests
```

Expected: both test suites pass independently and Ruff reports no lint or formatting errors.

- [ ] **Step 4: Confirm the worktree and lock are clean**

Run:

```sh
pixi install --locked -e dataset-ci
pixi install --locked -e trainer-ci
git status --short --branch
git log --oneline --max-count=8
```

Expected: both locked installs succeed without rewriting `pixi.lock`, no uncommitted changes remain, and the commit series contains only target inventory, Pixi configuration, docs, and CI changes.

## Task 6: Publish the tested branch to the fork

**Files:**
- Remote branch: `aeroaks/issue-9-uv-workspaces`

**Interfaces:**
- Publish the feature branch to the user's fork remote `aeroaks`.
- Do not modify the fork's `main` or upstream `origin/main`.

- [ ] **Step 1: Push the tested branch to the fork**

From the issue worktree, run:

```sh
git push -u aeroaks issue-9-uv-workspaces
```

- [ ] **Step 2: Verify the published branch**

Run:

```sh
git ls-remote --heads aeroaks issue-9-uv-workspaces
git rev-parse HEAD
```

Expected: the remote branch SHA equals local `HEAD`. The eventual pull request should target `satyrn-ai/satyrn-models`.
