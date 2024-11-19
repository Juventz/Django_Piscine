#!/bin/bash

echo "Setting up Django environment"
python3 -m venv django_env

source django_env/bin/activate

echo "Installing requirements"
pip install --upgrade pip
pip install --upgrade -r requirements.txt

echo "Setting up Django"
cd d05
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py runserver