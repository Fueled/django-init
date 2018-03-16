#!/bin/bash

# Setup for returning a non-zero exit code if any of the command fails.
err=0
trap 'err=1' ERR

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
ansible-playbook -i provisioner/hosts provisioner/site.yml --syntax-check
source venv/bin/activate
flake8
fab test:"--cov"
# Running 2to3 to ensure python3 compatible code is written
2to3 hello_world

test $err = 0 # Return non-zero if any command failed
