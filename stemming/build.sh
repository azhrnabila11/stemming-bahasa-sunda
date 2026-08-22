#!/usr/bin/env bash
# exit on error
set -o errexit

python3.11 -m pip install -r requirements.txt

python3.11 manage.py collectstatic --noinput --clear
python manage.py migrate

