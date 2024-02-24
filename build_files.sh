#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Create the dist directory if it doesn't exist
mkdir -p dist

# Collect static files into the dist directory
python3.7 manage.py collectstatic --no-input

# Exit with success status
exit 0
