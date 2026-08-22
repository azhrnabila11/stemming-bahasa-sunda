#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
python manage.py migrate --noinput

