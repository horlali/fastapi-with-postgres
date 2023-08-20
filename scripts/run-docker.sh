#!/bin/sh

set -e

# Go to root folder
cd $(dirname $0)/..


# Environment options
ENV_FILE=".env"
DAEMON=""


if [ "$1" = "-d" ];
    then
        echo "Running as daemon"
        DAEMON="-d"
fi


docker compose -f docker-compose.yml --env-file ${ENV_FILE} up ${DAEMON} --build
