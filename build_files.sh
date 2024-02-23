#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Create the staticfiles_build directory if it doesn't exist
mkdir -p staticfiles_build

# Collect static files
python3.9 manage.py collectstatic --no-input

# Exit with success status
exit 0
