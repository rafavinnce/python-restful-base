# Django Restful API
API responsible for applying the intelligence and business rules of the Application project.

## Installation

### Requirements

* Python (2.7, 3.4, 3.5, 3.6, 3.7 >)
* Django (1.11, 2.0, 2.1 >)

### Clone

Execute the following command to get the latest version of the project:

```terminal
$ git clone git@github.com:rafaelmilanibarbosa/python-restful-base.git python-restful-base
```

### Setup the local virtual environment
```terminal
cd python-restful-base
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
