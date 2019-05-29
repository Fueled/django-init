#!/bin/bash

# Setup for returning a non-zero exit code if any of the command fails.
err=0
trap 'err=1' ERR

# Clean
# if psql -lqt | cut -d \| -f 1 | grep -qw hello_world ; then
#     read -p "Database 'hello_world' required for running the tests already exist. Do you want to delete it (y)?" yn
#     if echo "$yn" | grep -iq "^n" ;then
#         exit
#     else
#         dropdb hello_world
#     fi
# fi

# rm -rf hello-world-web/;

# Generate new code, (it also creates db, migrate and install dependencies)
yes 'y' | cookiecutter . --no-input

# Run the tests present inside generate project
cd hello-world-web;
npm run build
ansible-playbook -i provisioner/hosts provisioner/site.yml --syntax-check
fab test:"--cov"

# Cleanup
# dropdb hello_world

test $err = 0 # Return non-zero if any command failed
