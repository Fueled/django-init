cookiecutter-django
==============================

Project base for backend projects used at Fueled

Features
--------

* Django 1.6
* PostresSQL 9.3
* Foundation 4
* SASS, CoffeeScript, Live-Reloading Server
* Vagrant box, Ansible
* Heroku - Sendgrid, Newrelic
* Amazon EC2, RDS, ElasticCache, SQS, SES

Getting Started
----------------

You need to have `cookiecutter` installed in order to scafold a new project from this template. If you have `pip` installed, you simply do this by running:

    sudo pip install cookiecutter==0.7.0

After the installation is successful, you can create a new django project by running:

    cookiecutter https://github.com/Fueled/cookiecutter-django.git

After cloning the repo, it will ask a bunch of questions and will a create a new folder with the value of `repo_name` you provided, containing the project base code and documentation to start working with your new project further.
