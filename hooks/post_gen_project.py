"""Post-generation hook: initializes Git, optional tools, and prints next steps."""

import os
import subprocess
import shutil


def run(cmd: list[str]) -> None:
    """Run a shell command, suppressing errors gracefully."""
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass


def remove_file(filepath: str) -> None:
    """Remove a file if it exists."""
    if os.path.isfile(filepath):
        os.remove(filepath)


def remove_dir(dirpath: str) -> None:
    """Remove a directory if it exists."""
    if os.path.isdir(dirpath):
        shutil.rmtree(dirpath)


# --- Conditional file cleanup ---

# Remove Docker files if not selected
if "{{ cookiecutter.include_docker }}" == "no":
    remove_file("docker-compose.yaml")
    remove_dir("dockerfiles")

# Remove GitHub Actions if not selected
if "{{ cookiecutter.include_github_actions }}" == "no":
    remove_dir(".github")

# Remove Hydra configs if not selected
if "{{ cookiecutter.include_hydra }}" == "no":
    remove_dir("configs")

# Remove FastAPI scaffold if not selected
if "{{ cookiecutter.include_fastapi }}" == "no":
    remove_dir("api")

# --- Initialize Git ---
run(["git", "init"])
run(["git", "add", "."])
run(["git", "commit", "-m", "Initial project structure from SE 489 MLOps template"])

# --- Initialize DVC if selected ---
if "{{ cookiecutter.use_dvc }}" == "yes":
    run(["dvc", "init"])

# --- Print next steps ---
print(
    """
================================================================================
    SE 489 MLOps Project — {{ cookiecutter.project_name }}
================================================================================

Your project has been created successfully!

Next steps:
  1. cd {{ cookiecutter.repo_name }}
  2. Create a virtual environment:
       python -m venv .venv
       source .venv/bin/activate   # macOS/Linux
       .venv\\Scripts\\activate      # Windows
     Or with uv (recommended):
       uv venv && source .venv/bin/activate
  3. Install dependencies:
       pip install -r requirements.txt   # or: uv pip install -r requirements.txt
       pip install -e ".[dev]"           # development tools
  4. Set up pre-commit hooks:
       pre-commit install
  5. Connect to your GitHub remote:
       git remote add origin https://github.com/<your-username>/{{ cookiecutter.repo_name }}.git
       git push -u origin main

Phase deliverables: see PHASE1.md, PHASE2.md, PHASE3.md
================================================================================
"""
)
