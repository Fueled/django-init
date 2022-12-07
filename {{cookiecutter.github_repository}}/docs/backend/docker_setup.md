# Getting Up and Running Locally With Docker

The steps below will get you up and running with a local development environment. All of these commands assume you are at the root of your generated project.

## Prerequisites

- `Docker`; if you don’t have it yet, follow the [installation instructions](https://docs.docker.com/install/#supported-platforms).
- `Docker Compose`; refer to the official documentation for the [installation guide](https://docs.docker.com/compose/install/).

## Build the Stack

This can take a while, especially the first time you run this particular command on your development system. Make sure to generate a `poetry.lock` file the first time you are running the project

```BASH
$ poetry lock
```

then you can build the containers using:

```bash
$ docker-compose -f local.yml build
```

For local env, use `local.yml`, for production use `production.yml` and then execute specific commands necessary.

## Run the Stack

This brings up both Django and PostgreSQL. The first time it is run it might take a while to get started, but subsequent runs will occur quickly.

```bash
$ docker-compose -f local.yml up
```

To run in a detached (background) mode, just:

```bash
$ docker-compose up -d
```

## Execute Management Commands

As with any shell command that we wish to run in our container, this is done using the `docker-compose -f local.yml run --rm` command:

```bash
$ docker-compose -f local.yml run --rm django python manage.py migrate
$ docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

Here, `django` is the target service (from the docker-compose file) we are executing the commands against.

## Debugging

### ipdb

If you are using the following within your code to debug:

```bash
import ipdb; ipdb.set_trace()
```

Then you may need to run the following for it to work as desired:

```bash
$ docker-compose -f local.yml run --rm --service-ports django
```

### docker

The `container_name` from the yml file can be used to check on containers with docker commands, for example:

```bash
$ docker logs worker
$ docker top worker
```

## Celery Flower

[Flower](https://github.com/mher/flower) is a “real-time monitor and web admin for Celery distributed task queue”.

By default, it’s enabled both in local and production environments (`local.yml` and `production.yml` Docker Compose configs, respectively) through a `flower` service. For added security, `flower` requires its clients to provide authentication credentials specified as the corresponding environments’ `.envs/.local/.django` and `.envs/.production/.django` `CELERY_FLOWER_USER` and `CELERY_FLOWER_PASSWORD` environment variables. Check out `localhost:5555` and see for yourself.

# Database Maintenance Scripts

There are three maintenance scripts present in the PostgreSQL container.

- `backup`: It uses pg_dump to create a backup of the current database with the created timestamp in the filename with a file ending with `.sql.gz`.
- `backups`: It lists all the backups present for the current database.
- `restore`: It **DROPS** the current database and then creates a new database with the chosen backup file.

For running any of the database maintenance scripts, you can use `run --rm` option for docker-compose file like:

```
docker-compose -f dev.yml run --rm postgres backups
```

This would use the Postgres container and execute the `backups` script to list all backups.

Similarly for creating a backup for the database, use:

```
docker-compose -f dev.yml run --rm postgres backup
```

and for restore use:

```
docker-compose -f dev.yml run --rm postgres restore <name-of-backup-file>
```

Make sure to replace `<name-of-backup-file>` in the above command with the name of the file you want to backup with. You can get these filenames via `backups` command.
