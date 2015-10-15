#!/bin/bash

# Setup
createdb hello_world
if [ $? -ne 0 ]; then
    read -p "Database 'hello_world' required for running the tests already exist. Do you want to delete it (y)?" yn
    if echo "$yn" | grep -iq "^n" ;then
        exit
    else
        dropdb hello_world
        createdb hello_world
    fi
fi
rm -rf hello-world-web/;
yes 'y' | cookiecutter . --no-input

# Run the tests present inside generate project
cd hello-world-web;
source venv/bin/activate
fab test:"--cov"
