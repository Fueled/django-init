{{ cookiecutter.project_name }}
==============================

{{ cookiecutter.project_description }}

Features
--------

* Django 1.7
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

1. Clone this repo to your local development machine.

    ```
    git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_reponame }}.git && cd {{ cookiecutter.github_reponame }}
    ```

2. Install `fab` command

    sudo pip install fabric

3. From inside the project repo, run `fab init`

5. Go grab a cup of coffee, till your hot development machine is baking!!


## Deploying Project

The deployment are managed via travis, but for the first time you'll need to set the configuration values on each of the server.

### Heroku

Run these commands to deploy a new project to Heroku:

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
heroku run python {{ cookiecutter.repo_name }}/manage.py migrate
heroku run python {{ cookiecutter.repo_name }}/manage.py createsuperuser
heroku open
```

### AWS

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptas, rem, ipsum. Perferendis, voluptatum reiciendis molestias fugit voluptatibus temporibus vitae fuga expedita laboriosam totam minus ea voluptatem a eligendi incidunt veritatis.


## Contributing

Refer to [CONTRIBUTING.md][contributing]

[contributing]: http://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_reponame}}/tree/master/CONTRIBUTING.md

--------
Built with ♥ at [Fueled](http://fueled.com)
