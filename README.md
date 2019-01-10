# Beblue Logger Service API
Django Restful API responsible for applying the intelligence and business rules of the Logger project.

## Installation

### Requirements

* Python (2.7, 3.4, 3.5, 3.6, 3.7 >)
* Django (1.11, 2.0, 2.1 >)
* Virtual Env (Arch Linux package - pacman -S python-virtualenv - [info here](https://www.archlinux.org/packages/?name=python-virtualenv))

### Clone

Execute the following command to get the latest version of the project:

```terminal
$ git clone git clone git@bitbucket.org:beblue/logger-service.git logger-service
```

### Setup the local virtual environment
```terminal
cd logger-service
virtualenv env
source env/bin/activate
pip install django
pip install djangorestframework
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
```

## Run
### Run local server
```terminal
./manage.py runserver
```
The base address of RESTful API is [http://127.0.0.1:8000](http://127.0.1:8000)

## Tests
### Run the tests
```terminal
./runtests.py
```

We **highly recommend** and only officially support the latest patch release of
each Python and Django series.



Full documentation for Django can be found on the [Django website](http://laradock.io/).

Django Rest Framework [Django Rest Framework](https://www.django-rest-framework.org).
