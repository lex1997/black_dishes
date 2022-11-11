#!/bin/sh


## DEV data creation

python manage.py makemigrations
python manage.py migrate
python manage.py fill_categories
python manage.py fill_dishes


exec "$@"
