#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate migration files for your apps
# This creates the "instructions" for the database tables
python manage.py makemigrations accounts
python manage.py makemigrations

# 3. Apply database migrations
# This actually builds the tables in PostgreSQL
python manage.py migrate

# 4. Convert static files for production
python manage.py collectstatic --no-input