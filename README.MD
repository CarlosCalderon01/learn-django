# learn-django

- the objetive for this project is learn and practice alls methods backend for use in django.

- 

# Strucuture Folders

- mysite: is a main folder.

- myapp: is for learn and test only use django

- quickstart: is for learn and test  DjangoRestFramework

# Commands List

## Virtual Env

- pip install virtualenv

    - (Version > 3.3):
        - python -m venv venv
    - (Version <= a 3.3):
        - virtualenv venv

- How to activate & deactivate

    Activate:
        venv\Scripts\activate.bat
    Deactivate:
        deactivate or venv\Scripts\deactivate.bat

## Basic to Install

- Django-admin --version
- pip --version

- pip install django
- python.exe -m pip install --upgrade pip

## Dependencyes

- (List all dependency + Lib OS)
    pip list
- // (Dependency production.)
    pip freeze > requirements.txt
- // (Install all dependency)
    pip install -r requirements.txt

## Django

- django-admin startproject learn-django . // (Create New Project)
    - python manage.py startapp quickstart // (Create new App)
    - django-admin startapp quickstart

- python manage.py makemigrations // (Create models)
- python manage.py migrate // (Send Models of table)

### Models

- python manage.py inspectdb > models.py
- python manage.py inspectdb nametable
- python manage.py createsuperuser

### DjangoRestFraework

- pip install djangorestframework
- pip install markdown
- pip install django-filter

# Bibliography:

