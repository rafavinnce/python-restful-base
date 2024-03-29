# Python Restful Logger Service API
Django Restful API responsible for applying the intelligence and business rules of the Logger project.

## Installation

### Requirements

* Python (2.7, 3.4, 3.5, 3.6, 3.7 >)
* Django (1.11, 2.0, 2.1 >)
* Virtual Env (Arch Linux package - pacman -S python-virtualenv - [info here](https://www.archlinux.org/packages/?name=python-virtualenv))

### Clone

Execute the following command to get the latest version of the project:

```terminal
$ git clone git clone git@github.com:rafaelmilanibarbosa/python-restful-base.git python-restful-base
```

### Setup the local virtual environment
```terminal
cd python-restful-base
cp -R .env.example .env # rename variables with own values
docker-compose up --build -d
docker-compose exec logger_service python manage.py migrate 
docker-compose exec logger_service python manage.py createsuperuser 
```

## Run
### Run local server
The base address of RESTful API is [http://127.0.0.1:8000](http://127.0.1:8000)
```terminal
curl -H 'Accept: application/json; indent=4' -u your_uer:'your_pass' http://127.0.0.1:8000/

or without auth user

curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/health/

```

## Tests
### Run the tests
```terminal
./runtests.py
```

We **highly recommend** and only officially support the latest patch release of
each Python and Django series.



Full documentation for Django can be found on the [Django website](http://laradock.io/).

Django Rest Framework [Django Rest Framework](https://www.django-rest-framework.org).
