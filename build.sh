#!/bin/sh
python manage.py makemigrations webapp

python manage.py migrate

python manage.py sqlmigrate webapp 0001

python webapp/importJSON.py

python manage.py loaddata output.json