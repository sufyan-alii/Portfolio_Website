#!/bin/bash
# Collect static files only (Vercel will install requirements automatically)
python3 manage.py collectstatic --noinput --clear
