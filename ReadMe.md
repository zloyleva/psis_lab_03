# Lab 03

### Create a virtualenv to isolate our package dependencies locally
virtualenv lab_03

source lab_03/bin/activate

### Install Django and Django REST framework into the virtualenv (If it need)
pip install django
pip install djangorestframework

pip freeze > requirements.txt

# Set up a new project
django-admin startproject lab03_project .
cd lab03_project 

### Create single application
django-admin startapp port_control

### Running migrations:
python manage.py migrate

### Create superuser
python manage.py createsuperuser --email admin@example.com --username admin

In /settings.py Add 'rest_framework' to INSTALLED_APPS.

```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```