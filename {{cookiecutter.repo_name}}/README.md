{{ cookiecutter.project_name }}
==============================

{{ cookiecutter.project_description }}

Features
--------

* Django 1.6
* PostresSQL 9.3
* Foundation 5
* SASS, CoffeeScript, Live-Reloading Server
* Vagrant box, Ansible
* Heroku/Sendgrid/S3
* Project configuration based on [http://12factor.net](http://12factor.net)


## Getting up and running

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv
* PostgreSQL

First make sure to create and activate a virtualenv, then open a terminal at the project root and install the requirements for local development:

1. Clone this repo to your local development machine.

	```
    git clone {{ cookiecutter.repo_url }} && cd {{ cookiecutter.repo_name }}
    ```

2. Install `fab` command

	```
    sudo pip install fabric
    ```

3. Setup the required environment variables

	```
	fab config:set,DJANGO_DATABASE_URL,[value]
	```
	* URL Format Ref: https://github.com/kennethreitz/dj-database-url#url-schema

4. From inside the project repo, run `fab init`, it will ask your system password.

5. Go grab a cup of coffee, till your hot development machine is baking!!



## Deploying Project

### Heroku

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
heroku config:set DJANGO_AWS_ACCESS_KEY_ID=YOUR_ID
heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY=YOUR_KEY
heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME=YOUR_BUCKET_NAME
git push heroku master
heroku run python {{cookiecutter.repo_name}}/manage.py syncdb --noinput
heroku run python {{cookiecutter.repo_name}}/manage.py migrate
heroku run python {{cookiecutter.repo_name}}/manage.py createsuperuser
heroku open
```


### AWS

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptas, rem, ipsum. Perferendis, voluptatum reiciendis molestias fugit voluptatibus temporibus vitae fuga expedita laboriosam totam minus ea voluptatem a eligendi incidunt veritatis.


--------

Built with ♥ at [Fueled](http://fueled.com)
