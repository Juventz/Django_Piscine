#!/bin/bash

echo "Setting up PostgreSQL database and role"
./setup_db.sh

echo "Setting up Django environment"
python3 -m venv django_env

source django_env/bin/activate

echo "Installing requirements"
pip install --upgrade pip
pip install --upgrade -r requirements.txt

echo "Checking pg_config availability"
if ! command -v pg_config &> /dev/null
then
    echo "pg_config could not be found, installing libpq-dev..."
    sudo apt update
    sudo apt install -y libpq-dev
fi

echo "Setting up Django"
cd ORM

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
