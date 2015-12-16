cookiecutter-django
====================

[![Build Status](https://travis-ci.org/Fueled/cookiecutter-django.svg?branch=user-app)](https://travis-ci.org/Fueled/cookiecutter-django)

Project template for django based projects, optimized for making REST API with deployment on Heroku and EC2 instances.

## Features

- Django 1.9.x
- PostresSQL everywhere.
- [Procfile] for deploying to Heroku.
- [Ansible] script for quick deployment to Ubuntu based servers.
- [12-Factor][12factor] based settings management via [django-environ], reads settings from `.env` if present.
- Designed to work with Django Rest Framework 3.0+.
- Uses `django_sites` instead of `django.contrib.sites`
- Use [mkdocs] for project documentation.
- Uses [py.test] as test runner.
- `travis.yml` for running isolated tests and deployments to dev/qa/prod environment on Heroku from git branches.
- Custom User app, for easier extensibility.
- Optional media storage using Amazon S3
- robots.txt and humans.txt configured

## Getting Started

You need to have `cookiecutter` installed in order to scafold a new project from this template.

```
cookiecutter gh:Fueled/cookiecutter-django
```

It will ask you to some questions, after which it will create a new project in your current working directory. It will also create a virtualenv in the folder `venv` inside the project, and install all the python dependencies inside it.

Once the cookiecutter script finishes, you'll have:

1. A postgres database created, with name same as `main_module` you provided.
2. Installed all the python dependencies in virtualenv
3. Local settings added to `.env` file (untracked)
4. Initialized a git repo and created the first commit.

Now the only thing you'll need to do is:

1. `cd` into the new `github_repository` folder just created.
2. Activate virtualenv `source venv/bin/activate`. If you plan to use virtualenvwrapper, you can install the project requirements via `pip install -r requirements/development.txt`
3. Run `fab serve`

__Summarizing__:

```
brew install postgres
[sudo] pip install fabric cookiecutter
cookiecutter gh:Fueled/cookiecutter-django
cd <github_repository>/
git init; git add .
git commit -m "Initial commit."
source venv/bin/activate
fab serve
```

Don't forget to carefully look at the generated README. Awesome, right?

You can also explore the [wiki] section for details on advance setups and usuages.

## Changelogs

Refer to [CHANGELOG.md](CHANGELOG.md).

--------

Built with ♥ at [Fueled](http://fueled.com)

[wiki]: https://github.com/Fueled/cookiecutter-django/wiki
[mkdocs]: http://www.mkdocs.org/
[12factor]: http://12factor.net
[py.test]: http://pytest.org/
[Procfile]: https://devcenter.heroku.com/articles/procfile
[django-environ]: https://github.com/joke2k/django-environ
[Ansible]: http://docs.ansible.com/index.html
