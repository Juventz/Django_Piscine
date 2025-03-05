#!/bin/bash

# Set up PostgreSQL database and role
echo "Setting up PostgreSQL database and role"

# Check if PostgreSQL is installed
if ! command -v psql &> /dev/null
then
    echo "PostgreSQL not found, installing PostgreSQL..."
    sudo apt update
    sudo apt install -y postgresql postgresql-contrib libpq-dev
fi

# Set up PostgreSQL database and role
sudo -u postgres psql -c "CREATE DATABASE djangotraining;"
sudo -u postgres psql -c "CREATE ROLE djangouser WITH LOGIN PASSWORD 'secret';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE djangotraining TO djangouser;"

# Set PostgreSQL password for the user
export PGPASSWORD=secret

echo "PostgreSQL setup complete. Database and user have been created."
