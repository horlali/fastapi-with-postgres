#!/bin/sh

set -e

# Go to backend folder
cd $(dirname $0)/..

NAME="FIDO-APP"
PROJECT_DIR="${PWD}/src/fido_app/"
MODULE_NAME="main:app"
PORT=8000
HOST=0.0.0.0

cd ${PROJECT_DIR}
echo "Starting ${NAME} server..."

uvicorn ${MODULE_NAME} \
    --host=${HOST} \
    --port=${PORT} \
    --reload
