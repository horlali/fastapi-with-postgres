#!/bin/sh

set -e

# Go to root folder
cd $(dirname $0)/..


# Environment options
if [ "$1" = "--dev" ];
    then
        ARGS=".env.dev"

elif [ "$1" = "--prod" ];
    then
        ARGS=".env.prod"

else
echo "Error: enviromnent not selected. Please add exactly one environment flag
to select an environment.
options:
    --dev: for development environment
    --prod: for production environment
"
    exit 128
fi


# Daemon option
DAEMON=""

if [ "$2" = "-d" ];
    then
        echo "Running as daemon"
        DAEMON="-d"
fi


docker compose -f docker-compose.yml --env-file ${ARGS} up ${DAEMON} --build
