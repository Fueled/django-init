#!/bin/bash

# Clean things up
rm -rf hello-world-web/; dropdb hello_world

# Generate project
yes 'y' | cookiecutter . --no-input

# Run the tests present inside generate project
cd hello-world-web;
source venv/bin/activate
fab test:""
