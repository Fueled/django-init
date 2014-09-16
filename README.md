cookiecutter-django
====================

Project base for backend projects

## Features

* Django 1.7
* PostresSQL 9.3
* Foundation 5
* SASS, CoffeeScript, Live-Reloading Server
* Vagrant box, Ansible
* Heroku/Sendgrid/S3
* [12factor][12factor] based project configuration

[mkdocs]: http://www.mkdocs.org/
[12factor]: http://12factor.net

## Getting Started

You need to have `cookiecutter` installed in order to scafold a new project from this template. If you have `pip` installed, you simply do this by running:

    pip install --upgrade cookiecutter

After the installation is successful, you can create a new django project by running:

    cookiecutter https://github.com/Fueled/cookiecutter-django.git

After cloning the repo, it will ask a bunch of questions and will a create a new folder with the value of `repo_name` you provided, containing the project base code and documentation to start working with your new project further.


- `cd` into the new `repo_name` folder and initialize a git a repo
- switch to the dev branch
- go to the repo directory and run `virtualenv --no-site-packages venv`.
 create a database in postgres named after the project, name is listed in settings file as `PROJECT_NAME`.
- set the privilege of that user as public, you can easily do it via pgadmin3.


### Production

#### Heroku

Run these commands to deploy the project to Heroku:

```
heroku create --buildpack https://github.com/heroku/heroku-buildpack-python
heroku addons:add heroku-postgresql:dev
heroku addons:add pgbackups:auto-month
heroku addons:add sendgrid:starter
heroku addons:add memcachier:dev
heroku pg:promote DATABASE_URL
heroku pg:promote DJANGO_CONFIGURATION=Production
heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32`
heroku config:set DJANGO_AWS_ACCESS_KEY_ID=PUT_YOUR_ID_HERE
heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY=PUT_YOUR_SECRET_KEY_HERE
heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME=PUT_BUCKET_NAME_HERE
git push heroku master
heroku run python {{cookiecutter.repo_name}}/manage.py migrate
heroku run python {{cookiecutter.repo_name}}/manage.py createsuperuser
heroku open
```

#### AWS

##### General Notes

* Micro EC2 instances always run the latest Ubuntu LTS release, currently 12.04.
* Use S3 for storing all media and static files. Use Django storages.
* One RDS instance for all DBs.

##### Preparing an Instance for a Client

Do these steps when handing over complete control of an instance to a client:

* TODO: Make a script called clean_instance.sh that remove logs, gets rid of repo files, private directory, etc... fill me in
* If deployment is still needed, instead of 'git pull' start using the fabric script.

## Coding Standards
* PEP8 should be used for all projects. http://www.python.org/dev/peps/pep-0008/
* The Google python style guide. Pay particular attention to the comments section: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
* Read over Two Scoops of Django


## GIT Branches
* There is a `master` and `dev` branch for each project.
* All developers should work off of the `dev` branch.
* If there is an unusual/new/innovative way of doing a new feature, create a branch off of `dev` and develop it there. After the feature is completed, ask another dev or a lead dev to review this added feature.


## Approved Libraries
This is a list of Python libraries or Django apps that have been tried and tested to be used for projects.

* [django-storages](http://django-storages.readthedocs.org/en/latest/) - for S3 as storage backend.
* [django-south](http://south.aeracode.org/)  (if using django <= 1.6):
* [django-grapelli](https://github.com/sehmaschine/django-grappelli)
* [django-rest-framework](http://www.django-rest-framework.org/) - for making REST API
* [python-social-auth](https://github.com/omab/python-social-auth)
* [python-requests](http://docs.python-requests.org/en/latest/)
* [python-dateutil](http://labix.org/python-dateutil)
* [python-user-agents](https://github.com/selwin/python-user-agents/)
* [django-versatileimagefield](https://github.com/WGBH/django-versatileimagefield)
* [django-extensions](http://django-extensions.readthedocs.org/)

--------

Built with ♥ at [Fueled](http://fueled.com)
