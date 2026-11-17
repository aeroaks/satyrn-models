# satyrn-models

Fine-tuning pipeline for SatyrnAI models.

## Training plan

Models go through three training stages, building on one another:

1. **CPT** (Continued Pretraining) - train on raw text.
2. **SFT** (Supervised Fine-Tuning) - train on prompt/response pairs.
3. **RL** (Reinforcement Learning) - train on a reward signal.

## Repository layout

- `corpus_builder/` - dataset generation (`satyrn-dataset` CLI)
- `trainer/unsloth/` - model fine-tuning (`satyrn-unsloth` CLI)
- `spikes/` - experiments which are not part of the main pipeline
- `datasets/`, `results/` - generated artifacts

## Quickstart

Environments are managed with [Pixi](https://pixi.sh). Each named environment installs one CLI, so dataset
generation and model training use separate environments. For example, to try the dataset CLI:

```sh
pixi install -e dataset-local
pixi run -e dataset-local satyrn-dataset --help
```

For target- and model-specific instructions:

1. Generating datasets - see [docs/dataset_generator.md](docs/dataset_generator.md).
2. Fine-tuning models - see [docs/trainer_unsloth.md](docs/trainer_unsloth.md).
3. Testing the Pixi environments locally and on Molab - see [docs/pixi_environment_testing.md](docs/pixi_environment_testing.md).
4. Running on Molab notebooks - see [docs/trainer_molab.md](docs/trainer_molab.md).
