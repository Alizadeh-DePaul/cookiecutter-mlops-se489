# API Reference

The package is importable as `{{ cookiecutter.repo_name }}` after running `pip install -e .`.

## `{{ cookiecutter.repo_name }}.config`

Project-wide path constants and typed config dataclasses.

```python
from {{ cookiecutter.repo_name }}.config import (
    PROJECT_ROOT,
    DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR,
    MODELS_DIR, REPORTS_DIR, FIGURES_DIR,
    Config, TrainingConfig, DataConfig, DEFAULT_CONFIG,
)
```

Use these constants instead of hard-coded relative paths — they resolve against the repo root regardless of the current working directory.

## `{{ cookiecutter.repo_name }}.logging_config`

```python
from {{ cookiecutter.repo_name }}.logging_config import setup_logging, get_logger

setup_logging(level="INFO")
logger = get_logger(__name__)
```

## `{{ cookiecutter.repo_name }}.data`

| Function | Purpose |
|---|---|
| `load_raw(filename)` | Read CSV from `data/raw/` |
| `load_processed(filename)` | Read CSV from `data/processed/` |
| `save_processed(df, filename)` | Write CSV to `data/processed/` |
| `process_data(input_dir, output_dir)` | Raw → processed pipeline |

CLI: `python -m {{ cookiecutter.repo_name }}.data.make_dataset [--input PATH] [--output PATH]`

## `{{ cookiecutter.repo_name }}.features`

```python
from {{ cookiecutter.repo_name }}.features import build_features

df_features = build_features(df_processed)
```

## `{{ cookiecutter.repo_name }}.models`

### `BaseModel` (abstract)

Abstract interface with `fit`, `predict`, `save`, `load`. Extend this for any new estimator.

### `Model`

Reference implementation scaffold. Serializes via `joblib`.

```python
from pathlib import Path
from {{ cookiecutter.repo_name }}.models import Model

model = Model(config={"lr": 0.01})
# model.fit(X_train, y_train)
model.save(Path("models/model.joblib"))
reloaded = Model.load(Path("models/model.joblib"))
```

## `{{ cookiecutter.repo_name }}.evaluation`

```python
from {{ cookiecutter.repo_name }}.evaluation import classification_report, regression_report

metrics = classification_report(y_true, y_pred)
# -> {"accuracy": ..., "precision": ..., "recall": ..., "f1": ...}
```

## `{{ cookiecutter.repo_name }}.visualization`

```python
from {{ cookiecutter.repo_name }}.visualization import plot_training_history, plot_confusion_matrix
```

## `{{ cookiecutter.repo_name }}.utils`

```python
from {{ cookiecutter.repo_name }}.utils import set_seed, save_json, load_json

set_seed(42)
```

## Training / Prediction CLIs

```bash
python -m {{ cookiecutter.repo_name }}.train_model --epochs 100 --batch-size 64
python -m {{ cookiecutter.repo_name }}.predict_model --model-path models/model.joblib --input data/processed/test.csv
```

{%- if cookiecutter.include_hydra == 'yes' %}

## Hydra Configuration

Configuration is managed through Hydra — see `configs/config.yaml` for defaults and override at runtime:

```bash
python -m {{ cookiecutter.repo_name }}.train_model model.name=custom_model training.epochs=200
```

{%- else %}

## Configuration

Defaults live in `{{ cookiecutter.repo_name }}.config.DEFAULT_CONFIG`. Override via CLI flags on the training/prediction entrypoints.

{%- endif %}

---

**{{ cookiecutter.project_name }}** · Version see `{{ cookiecutter.repo_name }}.__version__`
