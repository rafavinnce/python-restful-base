# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Copy in your requirements file
COPY requirements.txt /requirements.txt

# OR, if you’re using a directory for your requirements, copy everything (comment out the above and uncomment this if so):
COPY requirements /requirements

# Install base packages
RUN apk update
RUN apk upgrade
RUN apk add ca-certificates && update-ca-certificates

# Change TimeZone
RUN apk add --update tzdata
ENV TZ=America/Sao_Paulo

# Clean APK cache
RUN rm -rf /var/cache/apk/*

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step. Correct the path to your production requirements file, if needed.
RUN set -ex \
    && apk add --no-cache --update \
            python \
            python-dev \
            py-pip \
            gcc \
            make \
	        jq \
            libc-dev \
            musl-dev \
            linux-headers \
            pcre-dev \
            postgresql-dev \
    && pip install -U pip \
    && rm -rf /var/cache/apk/*

# Install pip dependencies
RUN pip install --no-cache-dir -r /requirements.txt

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir /logger-sevice/

# Set the working directory to /logger_service
WORKDIR /logger-service/

# Copy the current directory contents into the container at /logger_service
COPY . /logger-service/

# Add any custom, static environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=logger.settings.deploy

# uWSGI configuration (customize as needed):
ENV UWSGI_WSGI_FILE=logger/wsgi.py UWSGI_HTTP=:${SERVICE_PORT} UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# Get ECS random service port
RUN chmod +x /logger-service/random_service_port.sh && /logger-service/random_service_port.sh

# uWSGI will listen on this port
# EXPOSE 8000
EXPOSE ${SERVICE_PORT}

# Generate service id environment variable
RUN SERVICE_ID=logger-service-$(cat /proc/sys/kernel/random/uuid) && echo $SERVICE_ID > /logger-service/app.properties

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
RUN python manage.py collectstatic --noinput

# Startup Script
ENTRYPOINT ["/logger-service/entrypoint.sh"]

# Start uWSGI
CMD ["/venv/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]

