# {{ cookiecutter.project_name }}

**Version:** {{ cookiecutter.version }}

{{ cookiecutter.project_description }}

## Getting up and running

{% if cookiecutter.add_docker == 'y' %}
!!! note
For setting up locally using `Docker`, check [here](docs/backend/docker_setup.md)
{% endif %}

Minimum requirements: **pip, python3.9, poetry, redis & [PostgreSQL 11][install-postgres]{% if cookiecutter.add_postgis.lower() == "y" %} with postgis-2.4{% endif %}**, setup is tested on Mac OSX only.

```
brew install python3 poetry libmagic postgres {% if cookiecutter.add_postgis == 'y' %}postgis{% endif %}
```

[install-postgres]: http://www.gotealeaf.com/blog/how-to-install-postgresql-on-a-mac

In your terminal, type or copy-paste the following:

    git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository }}.git; cd {{ cookiecutter.github_repository }}; make install

Go grab a cup of coffee, we bake your hot development machine.

Useful commands:

- `make run` - start [django server](http://localhost:8000/)
- `make deploy_docs` - deploy docs to server
- `make test` - run the test locally with ipdb

**NOTE:** Checkout `Makefile` for all the options available and how they do it.

## Managing dependencies

### Poetry

To guarantee repeatable installations, all project dependencies are managed using [Poetry](https://python-poetry.org/). The project’s direct dependencies are listed in `pyproject.toml`.
Running `poetry lock` generates `poetry.lock` which has all versions pinned.

You can install Poetry by using `pip install --pre poetry` or by following the official installation guide [here](https://github.com/python-poetry/poetry#installation).

_Tip:_ We recommend that you use this workflow and keep `pyproject.toml` as well as `poetry.lock` under version control to make sure all computers and environments run exactly the same code.


## Deploying Project

The deployment are managed via travis, but for the first time you'll need to set the configuration values on each of the server.

Check out detailed server setup instruction [here](docs/backend/server_config.md).

{% if cookiecutter.add_fly == 'y' %}

### Develop on Fly.io

Create a [fly.io](https://fly.io) account.

Install `flyctl` and run the following commands to set up the Fly.io application, it will ask a series of questions regarding deployment configuration.

```
brew install flyctl
fly lauch
```

When ready to deploy, simply run the command using the Fly Dockerfile:

```
flyctl deploy --dockerfile ./compose/fly/django/Dockerfile
```

There is also a Github Action provided `.github/workflows/fly.yml` to deploy the application on the `master` branch. In order to deploy from CI:

1. Create Fly Access Token [here](https://fly.io/user/personal_access_tokens).
2. Add the `FLY_API_TOKEN` to the Github repo secrets [here](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repository}}/settings/secrets/actions)

{% endif %}

## How to release {{ cookiecutter.project_name }}

Execute the following commands:

```
git checkout master
make test
bump2version patch  # 'patch' can be replaced with 'minor' or 'major'
git push origin master
git push origin master --tags
git checkout qa
git rebase master
git push origin qa
```

## Contributing

Golden Rule:

> Anything in **master** is always **deployable**.

Avoid working on `master` branch, create a new branch with meaningful name, send pull request asap. Be vocal!

Refer to [CONTRIBUTING.md][contributing]

[contributing]: http://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repository}}/tree/master/CONTRIBUTING.md
