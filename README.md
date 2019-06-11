django-init | [![Build Status](https://travis-ci.com/Fueled/django-init.svg?branch=master)](https://travis-ci.com/Fueled/django-init)
============

Project template for django based projects, optimized for making REST API with deployment on Heroku and EC2 instances via Ansible.

## Features

- Django 2.2.x
- Python 3.6.x
- [12-Factor][12factor] based settings management via [django-environ], reads settings from `.env` if present.
- Supports PostreSQL 11.0 (support of postgis-2.5 is available).
- Ready to deploy on Heroku (optional) and Ubuntu 16 LTS via [Ansible](Optional)
- [Django Rest Framework][drf] 3.9.x. ready.
- Uses `django_sites` instead of `django.contrib.sites`
- Uses [mkdocs] for project documentation. Optionally, password protect the docs when deployed.
- Uses [pytest] as test runner.
- `travis.yml` for running isolated tests and deployments to dev/qa/prod environment on Heroku from git branches.
- Custom `User` app, for easier extensibility.
- Custom `Auth` app with JWT based Token Backend system with `login`, `logout` and `current_user_profile` modification views for easier extensibility.
- Media storage using Amazon S3 (optional)
- [Letsencrypt](https://letsencrypt.org/) Support via [certbot](https://certbot.eff.org)
- Static assets handling via webpack (optional)
- robots.txt and humans.txt configured

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
- try to create a postgres database and run the initial migration against it.

then only thing you'll need to do is:

1. `cd` into the new `github_repository` folder just created.
2. Activate virtualenv `source venv/bin/activate`.
3. Run `fab serve` or `./manage.py runserver`

Don't forget to carefully look at the generated README. Awesome, right?

You can also explore the [wiki] section for details on advance setup and usages.

## Articles

- [Setting up Django projects in a breeze](https://medium.com/fueled-engineering/setting-up-django-projects-in-a-breeze-36c715cc9a6f)

## Release Policy

`django-init` is a rolling release project. Commit and fixes are added to `master` branch on regular basis and always have latest stable django and associated libraries. You are advised to follow-up with changelogs.

## Changelogs

Refer to [CHANGELOG.md](CHANGELOG.md).

## Code of Conduct

Everyone interacting in the django-init project's codebase, issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).

## Related Projects

- https://github.com/pydanny/cookiecutter-django
- https://github.com/wemake-services/wemake-django-template
- https://github.com/lionheart/django-template

--------

Built with ♥ at [Fueled](https://fueled.com)

[wiki]: https://github.com/Fueled/django-init/wiki
[mkdocs]: http://www.mkdocs.org/
[12factor]: http://12factor.net
[pytest]: http://pytest.org/
[django-environ]: https://github.com/joke2k/django-environ
[Ansible]: http://docs.ansible.com/index.html
[devrecargar]: https://github.com/scottwoodall/django-devrecargar
[drf]: http://www.django-rest-framework.org/
