<p align="center">
  <img src="https://raw.githubusercontent.com/Fueled/django-init/master/.github/django-init-logo.png">
</p>

<p align="center">
<strong>django-init</strong> is a project boilerplate for Django based projects.
</p>

<p align="center">
    <a href="https://travis-ci.com/Fueled/django-init"><img src="https://travis-ci.com/Fueled/django-init.svg?branch=master" alt='Build Status'></a>
</p>

## Features

- Django 3.2.x
- Python 3.9.x
- [Poetry][poetry] Support
- Support for [black](https://pypi.org/project/black/)!
- [12-Factor][12factor] based settings management via [django-environ], reads settings from `.env` if present.
- Supports PostreSQL 13.0 (support of postgis-3.0 is available).
- [Django Rest Framework][drf] 3.13.x.
- Uses `django_sites` instead of `django.contrib.sites`.
- Uses [mkdocs] for project documentation. Optionally, password protect the docs when deployed via Ansible
- Uses [pytest] as test runner.
- Github Actions
- Custom `User` app, for easier extensibility.
- Custom `Auth` app with JWT based Token Backend system with `login`, `logout` and `current_user_profile` modification views for easier extensibility.
- robots.txt and humans.txt configured.

### Optional
- Heroku Setup
- Ubuntu 20 LTS via [Ansible]
- Celery with flower integration.
- AWS S3 media storage
- [Letsencrypt](https://letsencrypt.org/) Support via [certbot](https://certbot.eff.org).
- Postgis Setup
- Newrelic
- Sentry
- pre-commit hooks


## Getting Started

Install cookiecutter with `brew install cookiecutter` or `pip install cookiecutter`.

```
cookiecutter gh:Fueled/django-init
```

It will ask you couple of questions required to generate the project. It will generate a folder containing all the files in your current working directory.

If you opt to setup the project automatically, it will also:
- initialize a git repo and bump initial tag and version.
- create a virtualenv in the folder `venv` inside the project.
- install all the python dependencies inside it.
- create `poetry.lock` file after resolving dependencies and then generate `requirements.txt` and `requirements_dev.txt` for production and dev use respectively, for backward-compatibility.
- create a postgres database and run the initial migration against it.

then only thing you'll need to do is:

1. `cd` into the new `github_repository` folder just created.
2. Run `make run` or activate virtualenv with `poetry shell` and run `./manage.py runserver`

Don't forget to carefully look at the generated README. Awesome, right?

You can also explore the [wiki] section for details on advance setup and usages.

## Managing dependencies

### Poetry

To guarantee repeatable installations, all project dependencies are managed using [Poetry](https://python-poetry.org/). The project’s direct dependencies are listed in `pyproject.toml`.
Running `poetry lock` generates `poetry.lock` which has all versions pinned.

You can install Poetry by using `pip install --pre poetry` or by following the official installation guide [here](https://github.com/python-poetry/poetry#installation).

*Tip:* We recommend that you use this workflow and keep `pyproject.toml` as well as `poetry.lock` under version control to make sure all computers and environments run exactly the same code.

### Other tools

For compatibility, `requirements.txt` and `requirements_dev.txt` can be updated by running

```bash
poetry export -f requirements.txt -o requirements.txt
poetry export -f requirements.txt -o requirements_dev.txt --with dev
```

or

```bash
make generate_requirements
```

## Articles

- [Setting up Django projects in a breeze](https://medium.com/fueled-engineering/setting-up-django-projects-in-a-breeze-36c715cc9a6f)

## Release Policy

`django-init` is a rolling release project. Commit and fixes are added to `master` branch on regular basis and always have latest stable django and associated libraries. You are advised to follow-up with changelogs.

## Changelogs

Refer to [HISTORY.md](HISTORY.md).

## Code of Conduct

Everyone interacting in the django-init project's codebase, issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).

## Related Projects

- https://github.com/pydanny/cookiecutter-django
- https://github.com/wemake-services/wemake-django-template
- https://github.com/lionheart/django-template

--------

Built with ♥ at [Fueled](https://fueled.com)

[wiki]: https://github.com/Fueled/django-init/wiki
[poetry]: https://python-poetry.org/docs/
[mkdocs]: http://www.mkdocs.org/
[12factor]: http://12factor.net
[pytest]: http://pytest.org/
[django-environ]: https://github.com/joke2k/django-environ
[Ansible]: http://docs.ansible.com/index.html
[drf]: http://www.django-rest-framework.org/
