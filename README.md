<p align="center">
  <img src="https://img.shields.io/badge/SE%20489-MLOps-0057B7?style=for-the-badge&logo=google-cloud&logoColor=white" alt="SE 489 MLOps"/>
  <img src="https://img.shields.io/badge/DePaul%20University-CDM-003DA5?style=for-the-badge&logo=google-scholar&logoColor=white" alt="DePaul CDM"/>
</p>

<h1 align="center">Cookiecutter MLOps Template</h1>

<p align="center">
  <strong>A production-ready project template for SE 489: Machine Learning Engineering for Production</strong>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.11%20|%203.12%20|%203.13-3776AB?logo=python&logoColor=white" alt="Python"></a>
  <a href="https://cookiecutter.readthedocs.io/"><img src="https://img.shields.io/badge/cookiecutter-%E2%89%A52.7-D4AA00?logo=cookiecutter&logoColor=white" alt="Cookiecutter"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT"></a>
  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff"></a>
  <a href="https://pre-commit.com/"><img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="Pre-commit"></a>
  <a href="https://github.com/Alizadeh-DePaul/cookiecutter-mlops-se489/actions"><img src="https://img.shields.io/github/actions/workflow/status/Alizadeh-DePaul/cookiecutter-mlops-se489/tests.yaml?label=CI&logo=github" alt="CI"></a>
</p>

---

## Overview

This [Cookiecutter](https://cookiecutter.readthedocs.io/) template scaffolds **production-ready MLOps projects** aligned with the three phases of **SE 489 — Machine Learning Engineering for Production** at DePaul University. It provides a structured starting point with modern tooling for reproducible ML development, containerization, experiment tracking, and cloud deployment.

**What you get out of the box:**

- Modular Python package with training, prediction, and data processing scripts
- Configurable ML framework (PyTorch, TensorFlow, or scikit-learn)
- Docker and Docker Compose setup for reproducible environments
- GitHub Actions CI/CD workflows with linting, type checking, and testing
- Experiment tracking integration (MLflow or Weights & Biases)
- Hydra-based configuration management
- DVC support for data versioning
- Pre-commit hooks with Ruff and mypy
- MkDocs documentation site
- Phase-specific deliverable checklists (PHASE1.md, PHASE2.md, PHASE3.md)

---

## Quick Start

### Prerequisites

- **Python** 3.11 or higher
- **Cookiecutter** 2.7 or higher
- **Git** installed and configured

### Installation

```bash
# Install cookiecutter
pip install cookiecutter

# Generate your project
cookiecutter https://github.com/Alizadeh-DePaul/cookiecutter-mlops-se489
```

You will be prompted to configure your project:

| Prompt | Description | Default |
|--------|-------------|---------|
| `project_name` | Human-readable project name | SE 489 MLOps Project |
| `repo_name` | Repository name (auto-generated) | *(from project_name)* |
| `author_name` | Your name or team name | — |
| `author_email` | Your DePaul email | your.email@depaul.edu |
| `description` | Brief project description | — |
| `python_version` | Target Python version | 3.11 |
| `open_source_license` | License type | MIT |
| `ml_framework` | ML framework | pytorch |
| `use_dvc` | Enable DVC for data versioning | no |
| `include_docker` | Generate Docker files | yes |
| `experiment_tracking` | Experiment tracking system | mlflow |
| `include_hydra` | Hydra configuration management | no |
| `include_github_actions` | CI/CD workflows | yes |
| `include_fastapi` | FastAPI service template | no |

### After Generation

```bash
cd <your-repo-name>

# Create virtual environment
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
# .venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
pip install -e ".[dev]"

# Set up pre-commit hooks
pre-commit install

# Connect to GitHub
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

> **Tip:** Use [uv](https://docs.astral.sh/uv/) for faster dependency installation: `pip install uv && uv pip install -r requirements.txt`

---

## Project Phases

This template is structured around the three project phases in SE 489. Each phase builds upon the previous one, progressively adding MLOps capabilities.

### Phase 1 — Project Design & Model Development

> **Focus:** Experimentation, version control, and reproducibility

- Organized Python package with clear separation of concerns
- Git-based version control with `.gitignore` optimized for ML
- Data management structure (`data/raw/`, `data/processed/`)
- Training and prediction scripts with argument parsing and logging
- Model class with `train`, `predict`, and `evaluate` interfaces
- Makefile with common commands (`make train`, `make test`, `make lint`)
- Environment management with `pyproject.toml`

**Deliverables:** See `PHASE1.md` in the generated project for the complete checklist.

### Phase 2 — Containerization & Monitoring

> **Focus:** Reproducible environments, experiment tracking, and profiling

- Dockerfile with multi-stage build for efficient container images
- Docker Compose for orchestrating training and serving containers
- MLflow or Weights & Biases integration for experiment tracking
- Hydra configuration management for hyperparameter tuning
- Structured logging with configurable log levels
- Performance profiling and optimization guidance

**Deliverables:** See `PHASE2.md` in the generated project for the complete checklist.

### Phase 3 — CI/CD & Deployment

> **Focus:** Testing, automation, and cloud deployment

- GitHub Actions workflows for automated testing, linting, and Docker builds
- pytest-based test suite with fixtures and coverage reporting
- CML (Continuous Machine Learning) integration for PR-based model evaluation
- FastAPI service template for model serving
- Cloud deployment guides for GCP (Cloud Run, Vertex AI, Cloud Functions)
- Streamlit/Gradio templates for HuggingFace Spaces deployment

**Deliverables:** See `PHASE3.md` in the generated project for the complete checklist.

---

## Generated Project Structure

```
<your-repo-name>/
├── <project_name>/                # Main Python package
│   ├── __init__.py
│   ├── train_model.py             # Training script
│   ├── predict_model.py           # Prediction script
│   ├── data/
│   │   ├── __init__.py
│   │   └── make_dataset.py        # Data processing
│   ├── models/
│   │   ├── __init__.py
│   │   └── model.py               # Model definitions
│   └── visualization/
│       ├── __init__.py
│       └── visualize.py           # Plotting utilities
├── data/
│   ├── raw/                       # Immutable raw data
│   └── processed/                 # Cleaned, transformed data
├── models/                        # Trained model artifacts
├── notebooks/                     # Jupyter notebooks for exploration
├── tests/                         # Unit and integration tests
│   ├── conftest.py                # pytest fixtures
│   └── test_model.py              # Model test template
├── docs/                          # MkDocs documentation
├── reports/figures/               # Generated plots and analysis
├── dockerfiles/Dockerfile         # Multi-stage Docker build
├── configs/config.yaml            # Hydra configuration (if selected)
├── api/                           # FastAPI service (if selected)
├── .github/workflows/ci.yml       # GitHub Actions CI/CD
├── PHASE1.md                      # Phase 1 deliverables checklist
├── PHASE2.md                      # Phase 2 deliverables checklist
├── PHASE3.md                      # Phase 3 deliverables checklist
├── .pre-commit-config.yaml        # Ruff + mypy + pre-commit hooks
├── Makefile                       # Common commands
├── docker-compose.yaml            # Docker Compose setup
├── pyproject.toml                 # Project config & dependencies
├── requirements.txt               # Runtime dependencies
├── requirements_dev.txt           # Development dependencies
└── LICENSE
```

---

## Template Options

All options are organized by the phase where they become most relevant:

| Option | Default | Choices | Phase |
|--------|---------|---------|-------|
| `python_version` | 3.11 | 3.11, 3.12, 3.13 | 1 |
| `ml_framework` | pytorch | pytorch, tensorflow, scikit-learn | 1 |
| `open_source_license` | MIT | MIT, BSD-3-Clause, No license file | 1 |
| `use_dvc` | no | yes, no | 2 |
| `include_docker` | yes | yes, no | 2 |
| `experiment_tracking` | mlflow | mlflow, wandb, none | 2 |
| `include_hydra` | no | yes, no | 2 |
| `include_github_actions` | yes | yes, no | 3 |
| `include_fastapi` | no | yes, no | 3 |

---

## Technology Stack

| Category | Tools |
|----------|-------|
| **Language & Packaging** | Python 3.11+, `pyproject.toml` (PEP 517/518), pip / uv |
| **ML Frameworks** | PyTorch, TensorFlow, or scikit-learn |
| **Containerization** | Docker, Docker Compose |
| **Code Quality** | Ruff (lint + format), mypy (type checking), pre-commit hooks |
| **CI/CD** | GitHub Actions |
| **Experiment Tracking** | MLflow or Weights & Biases |
| **Configuration** | Hydra + OmegaConf |
| **Data Versioning** | DVC (optional) |
| **Model Serving** | FastAPI, Streamlit, Gradio |
| **Cloud Deployment** | GCP Cloud Run, Vertex AI, HuggingFace Spaces |
| **Testing** | pytest, pytest-cov |
| **Documentation** | MkDocs with Material theme |

---

## Available Make Commands

Every generated project includes a `Makefile` with these targets:

```bash
make requirements       # Install runtime dependencies
make dev_requirements   # Install development dependencies
make data               # Run data processing pipeline
make train              # Train the model
make predict            # Generate predictions
make test               # Run pytest test suite
make lint               # Run Ruff linting and formatting checks
make format             # Auto-format code with Ruff
make clean              # Remove build artifacts and caches
make docker_build       # Build Docker image
make docker_run         # Run Docker container
make docs               # Serve MkDocs documentation locally
```

---

## Course Topics Covered

This template integrates the core SE 489 curriculum topics:

| Topic | Where in Template |
|-------|-------------------|
| Code organization & best practices | Project structure, `pyproject.toml`, Makefile |
| Version control | `.gitignore`, pre-commit hooks, branching guidelines |
| Data management | `data/` directory, DVC integration |
| Model development | `models/model.py`, `train_model.py`, `predict_model.py` |
| Containerization | `Dockerfile`, `docker-compose.yaml` |
| Experiment tracking | MLflow / W&B configuration |
| Configuration management | Hydra `configs/`, `config.yaml` |
| Profiling & debugging | Profiling guidance in PHASE2.md |
| Logging & monitoring | Structured logging in scripts |
| Testing | `tests/`, pytest, GitHub Actions CI |
| CI/CD pipelines | `.github/workflows/ci.yml`, CML |
| Cloud deployment | GCP guides, FastAPI service, PHASE3.md |
| Documentation | MkDocs, docstrings, README templates |

---

## License

This template is released under the [MIT License](https://opensource.org/licenses/MIT).

---

<p align="center">
  <strong>DePaul University — College of Computing and Digital Media</strong><br>
  SE 489: Machine Learning Engineering for Production (MLOps)
</p>
