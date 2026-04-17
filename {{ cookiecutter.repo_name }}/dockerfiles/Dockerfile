{%- if cookiecutter.include_docker == 'yes' %}
# Multi-stage build for {{ cookiecutter.project_name }}

# Stage 1: Builder
FROM python:{{ cookiecutter.python_version }}-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runtime
FROM python:{{ cookiecutter.python_version }}-slim

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local

# Set environment variables
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Copy project code
COPY . .

# Install the package
RUN pip install --no-cache-dir -e .

EXPOSE 8000

ENTRYPOINT ["python", "-m", "{{ cookiecutter.repo_name }}.train_model"]
{%- else %}
# Dockerfile for {{ cookiecutter.project_name }}
# Docker support disabled in project configuration
{%- endif %}
