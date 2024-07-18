#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
poetry install

# Convert static asset files
poetry run python manage.py collectstatic --no-input

# Apply any outstanding database migrations
poetry run python manage.py migrate