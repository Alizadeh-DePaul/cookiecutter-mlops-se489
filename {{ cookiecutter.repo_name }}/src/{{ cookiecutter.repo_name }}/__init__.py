"""{{ cookiecutter.project_name }}.

{{ cookiecutter.description }}
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{ cookiecutter.repo_name }}")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.author_email }}"

__all__ = ["__version__", "__author__", "__email__"]
