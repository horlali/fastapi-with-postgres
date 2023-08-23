#!/bin/sh

set -e

# Go to backend folder
cd $(dirname $0)/..

# Export environment variables
export DATABASE_URL=sqlite:///./db.sqlite3

# The --actions flag writes a coverage.xml file which is 
# used by GitHub Actions and CodeCov for coverage reports.
if [ "$1" = "--actions" ];
    then
        poetry run coverage run -m pytest -v
        poetry run coverage report --fail-under=80
        poetry run coverage xml

else
poetry run coverage run -m pytest -s -v
poetry run coverage report -m
fi
