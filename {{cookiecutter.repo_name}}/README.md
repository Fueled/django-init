{{cookiecutter.repo_name}}
==============================

{{cookiecutter.description}}

Features
--------
* Django 1.6
* Postgres 9.3
* Vagrant Development Box

Getting started
---------------

1. Clone this repo to your local development machine.

    git clone {{ cookiecutter.repo_url }} && cd {{ cookiecutter.repo_name }}

2. Install `fab` command
    
    sudo pip install fabric

3. From inside the project repo, run `fab init`, it will ask your system password.
4. Go grab a cup of coffee, till your hot development machine is baking!! 
