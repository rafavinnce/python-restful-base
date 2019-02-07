FROM python:3.7-alpine

# environments
ENV DJANGO_SECRET_KEY $SECRET_KEY
ENV DJANGO_DEBUG $DJANGO_DEBUG
ENV ALLOWED_HOSTS $ALLOWED_HOSTS

## Install base packages
RUN apk update
RUN apk upgrade

## Change TimeZone
ENV TZ=America/Sao_Paulo
RUN set -x \
    && apk add tzdata \
    && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
    && echo "America/Sao_Paulo" >  /etc/timezone

## Clean APK cache
RUN rm -rf /var/cache/apk/*

# Copy in your requirements file
ADD requirements.txt /requirements.txt

# OR, if you’re using a directory for your requirements, copy everything (comment out the above and uncomment this if so):
ADD requirements /requirements

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step. Correct the path to your production requirements file, if needed.
RUN set -ex \
    && apk add \
            gcc \
            make \
            libc-dev \
            musl-dev \
            curl \
            jq \
            linux-headers \
            pcre-dev \
            postgresql-dev \
    && pip install -U pip \
    && pip install -r /requirements.txt

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir /code/
WORKDIR /code/
ADD . /code/

# uWSGI will listen on this port
EXPOSE 8000

# uWSGI configuration (customize as needed):
ENV UWSGI_WSGI_FILE=logger/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
# RUN python manage.py
## RUN ddtrace-run python manage.py

RUN python manage.py

#RUN python manage.py migrate --noinput

## Startup Script
RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]

# Start uWSGI
CMD ["uwsgi", "--http-auto-chunked", "--http-keepalive"]
#CMD ["ddtrace-run", "uwsgi", "--http-auto-chunked", "--http-keepalive"]