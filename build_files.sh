#!/bin/bash

# Install Python dependencies
pip3 install -r requirements.txt

# Create the dist directory if it doesn't exist
mkdir -p dist
mkdir -p static


# Collect static files into the dist directory
python3.9 manage.py collectstatic --no-input

# Exit with success status
exit 0
