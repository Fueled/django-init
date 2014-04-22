cookiecutter-django
====================

Project base for backend projects used at Fueled

## Features
* Django 1.6
* PostresSQL 9.3
* Foundation 4
* Project documentation with [mkdocs][mkdocs]
* SASS, CoffeeScript, Live-Reloading Server
* Vagrant box, Ansible
* Heroku - Sendgrid, Newrelic
* Amazon EC2, RDS, ElasticCache, SQS, SES

[mkdocs]: http://www.mkdocs.org/

# Django/Python Devlopment 
Just a bunch of things about devloping, all in one place.


## Using boilerplate-web

TODO for this Repository:
* focus should be on re-usable apps: https://docs.djangoproject.com/en/1.6/intro/reusable-apps/
* add in mobile-password-reset as a re-usable app
* siteconfig as a re-usable app with a base SiteProfile class? Create an initial site object?
* how to handle having a base settings file for projects?


## Approved Libraries
This is a list of Python libraries or Django apps that have been tried and tested to be used for projects.
* django-storages for S3: http://django-storages.readthedocs.org/en/latest/
* django-south (if using django <= 1.6): http://south.aeracode.org/
* django-grapelli: https://github.com/sehmaschine/django-grappelli
* django-rest-framework (if making api): http://www.django-rest-framework.org/
* python-social-auth: https://github.com/omab/python-social-auth
* python-requests: http://docs.python-requests.org/en/latest/
* python-dateutil: http://labix.org/python-dateutil
* python-user-agents: https://github.com/selwin/python-user-agents/


## Configuring Django for Local Development

You need to have `cookiecutter` installed in order to scafold a new project from this template. If you have `pip` installed, you simply do this by running:

    sudo pip install cookiecutter==0.7.0

After the installation is successful, you can create a new django project by running:

    cookiecutter https://github.com/Fueled/cookiecutter-django.git

After cloning the repo, it will ask a bunch of questions and will a create a new folder with the value of `repo_name` you provided, containing the project base code and documentation to start working with your new project further.


* `cd` into the new `repo_name` folder and initialize a git repo `git init`
* switch to the dev branch
* go to the repo directory and run `virtualenv --no-site-packages venv`.
* create a database in postgres named after the project, name is listed in settings file as `PROJECT_NAME`.
* set the privilege of that user as public, you can easily do it via pgadmin3.


## Workflow for deploying project

# Heroku
 
Run these commands to deploy the project to Heroku:

```
heroku create --buildpack https://github.com/heroku/heroku-buildpack-python
heroku addons:add heroku-postgresql:dev
heroku addons:add pgbackups:auto-month
heroku addons:add sendgrid:starter
heroku addons:add memcachier:dev
heroku pg:promote HEROKU_POSTGRESQL_COLOR
heroku config:set DJANGO_CONFIGURATION=Production
heroku config:set DJANGO_SECRET_KEY=RANDOM_SECRET_KEY
heroku config:set DJANGO_AWS_ACCESS_KEY_ID=YOUR_ID
heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY=YOUR_KEY
heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME=YOUR_BUCKET_NAME
git push heroku master
heroku run python {{cookiecutter.repo_name}}/manage.py syncdb
heroku run python {{cookiecutter.repo_name}}/manage.py migrate
heroku run python {{cookiecutter.repo_name}}/manage.py createsuperuser
heroku open
```

# AWS

### General Notes
* Micro EC2 instances always run the latest Ubuntu LTS release, currently 12.04.
* Use S3 for storing all media and static files. Use Django storages.
* One RDS instance for all DBs.

### Preparing an Instance for a Client
Do these steps when handing over complete control of an instance to a client:
* TODO: Make a script called clean_instance.sh that remove logs, gets rid of repo files, private directory, etc... fill me in
* If deployment is still needed, instead of 'git pull' start using the fabric script. 

## Coding Standards
* PEP8 should be used for all projects. http://www.python.org/dev/peps/pep-0008/
* The Google python style guide. Pay particular attention to the comments section: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
* Read over Two Scoops of Django


## GIT Branches
* There is a master and dev branch for each project.
* All developers should work off of the dev branch.
* If there is an unusual/new/innovative way of doing a new feature, create a branch off of dev and develop it there. After the feature is completed, ask another dev or a lead dev to review this added feature.


## Configuring Django Admin Image Resizer
TODO: pje-fueled should fill this in.
