#!/bin/bash

pip_version=$(pip --version)
echo "Using pip version: $pip_version"

install_dir="local_lib"
log_file="install.log"

echo "Installing path.py in $install_dir..."
pip install --upgrade --target="$install_dir" "git+https://github.com/jaraco/path.git" &> "$log_file"

if [ $? -eq 0 ]; then
    echo "Path.py installed successfully!"
    python3 my_program.py
else
    echo "Installation failed. Check the log file for more information."
fi