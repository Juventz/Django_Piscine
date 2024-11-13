#!bin/bash

python3 -m venv django_venv

source django_venv/bin/activate

pip install --upgrade pip
pip install requirements.txt

echo "Django environment created and requirements installed"
exec bash
