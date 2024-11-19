#!/bin/bash

python3 -m venv django_env

source django_env/bin/activate

pip install --upgrade pip
pip install --upgrade -r requirements.txt

cd d05
python3 mamanage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py runserver