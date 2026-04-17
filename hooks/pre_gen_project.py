"""Pre-generation hook: validates project name before creating the project."""

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
repo_name = "{{ cookiecutter.repo_name }}"

if not re.match(MODULE_REGEX, repo_name):
    print(
        f"ERROR: '{repo_name}' is not a valid Python module name.\n"
        "Use only lowercase letters, numbers, and underscores.\n"
        "The name must start with a letter or underscore."
    )
    sys.exit(1)
