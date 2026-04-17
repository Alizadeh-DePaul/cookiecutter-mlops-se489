# Data Directory

Store all data files for the {{ cookiecutter.project_name }} project here.

## Structure

- **`raw/`** — Original, immutable data as received. Never modify files here.
- **`processed/`** — Cleaned, transformed, and feature-engineered data ready for modeling.

## Best Practices

{% if cookiecutter.use_dvc == "yes" -%}
- Use **DVC** to version large data files instead of Git
- Track `.dvc` files in Git; store actual data remotely
{% endif -%}
- **Never commit** large data files directly to Git
- Document data sources and transformations in notebooks or scripts
