"""Model definitions."""

from {{ cookiecutter.repo_name }}.models.base import BaseModel
from {{ cookiecutter.repo_name }}.models.model import Model

__all__ = ["BaseModel", "Model"]
