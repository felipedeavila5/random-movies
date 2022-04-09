#!/bin/bash
python manage.py migrate
python manage.py loaddata movies_api