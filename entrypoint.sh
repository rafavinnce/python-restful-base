#!/bin/sh
set -e

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    ddtrace-run python manage.py migrate --noinput
fi

if [ "x$DJANGO_MANAGEPY_COLLECTSTATIC" = 'xon' ]; then
    ddtrace-run python manage.py collectstatic --noinput
fi

# Run Consul Register Control
# python /logger-service/consul_script.py

exec "$@"