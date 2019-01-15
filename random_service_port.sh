#!/bin/bash

# ecs config
if [ "${ENVIRONMENT}" != "local" ]
    then
        export SERVICE_PORT=$(shuf -i 1024-65535 -n 1)
    else
        export SERVICE_PORT=6606
fi