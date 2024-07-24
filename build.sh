#!/usr/bin/env bash
# Exit on error
set -o errexit

sudo apt-get update && sudo apt-get install sqlite3

# Modify this line as needed for your package manager (pip, poetry, etc.)
poetry install

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate