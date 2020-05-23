# REST API

This app intends to be an REST API that shows data about "metrobus" of México City.

## DEPENDENCIES

- python3.8.3
- list of dependencies comes in requirements.txt
- optional a database like mariabd or postgres if you want to put this in production

### ENVIRONMENT VARIABLES

- SECRET_KEY
- DEBUG
- DEFAULT_DB
- ALLOWED_HOSTS
- LANGUAGE_CODE
- TIME_ZONE
- USE_I18N
- USE_L10N
- USE_TZ
- STATIC_URL
- STATIC_ROOT

can you set with a .env file, only put that file unde rest_project directory, [read why](https://django-environ.readthedocs.io/en/latest/).

## HOW TO INSTALL

run inside this project

```sh
pip install -r requirements.txt
```

for install dependencies

after set all environment variables

run with db running

```sh
./manage.py migrate
```

## HOW TO RUN

### DEVELOPMENT

after that you have installed and configured only left run

```sh
./manage.py runserver
```

### PRODUCTION

also you need to install via pip some server that understand wsgi python protocol I suggest use gunicorn or wsgi read in [django documentation](https://docs.djangoproject.com/en/3.0/howto/deployment/) about.

## RUN TESTS

```sh
./manage.py test
```

for run tests

## ROUTES

- GET /api/metrobus/
- GET /api/metrobus/{id}
- GET /api/district/
- GET /api/district/{id}
