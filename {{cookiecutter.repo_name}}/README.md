{{ cookiecutter.project_name }}
==============================

{{ cookiecutter.project_description }}

## Getting up and running

Minimum requirements: **pip, fabric & postgres**, setup is tested on Mac OSX only.

In your terminal, type or copy-paste the following:
    
    git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_reponame }}.git; cd {{ cookiecutter.github_reponame }}; fab init

Go grab a cup of coffee, we bake your hot development machine.

Useful commands:

- `fab serve` - start [django server](http://localhost:8000/), [documentation server](http://localhost:8001/) and static file compiler
- `fab webserver` - run only webserver 
- `fab deploy_docs` - deploy docs to server
- `fab test` - run the test locally with ipdb

**NOTE:** Checkout `fabfile.py` for all the options available and what/how they do it.


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
heroku config:set DJANGO_CONFIGURATION=Production
heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32`
heroku config:set DJANGO_AWS_ACCESS_KEY_ID=YOUR_ID
heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY=YOUR_KEY
heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME=YOUR_BUCKET_NAME
heroku config:set DJANGO_SITE_DOMAIN=DJANGO_SITE_DOMAIN_HERE
heroku config:set DJANGO_SITE_SCHEME=DJANGO_SITE_SCHEME_HERE
heroku config:set DJANGO_SITE_NAME=DJANGO_SITE_NAME_HERE
git push heroku master
heroku run python {{ cookiecutter.repo_name }}/manage.py migrate
heroku run python {{ cookiecutter.repo_name }}/manage.py createsuperuser
heroku open
```


## Contributing

Golden Rule:

> Anything in **master** is always **deployable**.

Avoid working on `master` branch, create a new branch with meaningful name, send pull request asap. Be vocal!

Refer to [CONTRIBUTING.md][contributing]

[contributing]: http://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_reponame}}/tree/master/CONTRIBUTING.md

--------
Built with ♥ at [Fueled](http://fueled.com)
