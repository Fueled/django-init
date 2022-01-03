.DEFAULT_GOAL := help
SHELL := bash
.ONESHELL:

PROJECT_NAME={{cookiecutter.main_module}}
DB_NAME=$(PROJECT_NAME)
INVENTORY=provisioner/hosts
PLAYBOOK=provisioner/site.yml
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('venv/bin/pip').exists(): print('venv/bin/')")


.PHONY: help
help:            ## show the help
	@echo "Usage: make <target>"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'


.PHONY: fmt
fmt:             ## Format code using black & isort.
	$(ENV_PREFIX)poetry run isort .
	$(ENV_PREFIX)poetry run black .


.PHONY: lint
lint:             ## Run pep8, black, mypy linters.
	$(ENV_PREFIX)poetry run flake8 .
	$(ENV_PREFIX)poetry run black --check .
	$(ENV_PREFIX)poetry run mypy --ignore-missing-imports ${PROJECT_NAME}/
	{% if cookiecutter.add_ansible.lower() == 'y' -%}
	$(ENV_PREFIX)poetry run ansible-playbook -i provisioner/hosts provisioner/site.yml --syntax-check
	{%- endif %}


run_all:  ## Run all the servers in parallel, requires GNU Make
	make -j django docs{% if cookiecutter.add_celery == 'y' %} celery{% endif %} redis
.PHONY: run_all

virtualenv:     ## Create a virtual environment.
	@echo "creating virtualenv ..."
	@rm -rf venv
	@python3 -m venv venv
	@./venv/bin/pip install -U pip poetry
	@echo
	@echo "!!! Please run 'source venv/bin/activate' to enable the environment !!!"


regenerate:  ## Delete and create new database.
	-dropdb $(DB_NAME)
	createdb $(DB_NAME)
	${ENV_PREFIX}python manage.py migrate
.PHONY: regenerate

update-libs:  ## update libs + generate new lockfile & requirements
	${ENV_PREFIX}poetry update
	${ENV_PREFIX}poetry export --without-hashes -f requirements.txt -o requirements_dev.txt --dev
	${ENV_PREFIX}poetry export --without-hashes -f requirements.txt -o requirements.txt
.PHONY: update-libs

install: virtualenv  ## Install and setup project dependencies
	${ENV_PREFIX}python -m pip install --upgrade pip wheel
	${ENV_PREFIX}poetry lock
	${ENV_PREFIX}poetry export --without-hashes -f requirements.txt -o requirements_dev.txt --dev
	${ENV_PREFIX}poetry export --without-hashes -f requirements.txt -o requirements.txt
	${ENV_PREFIX}poetry install
	${ENV_PREFIX}pre-commit install
ifneq ($(CI),True)
	-createdb $(DB_NAME)
	${ENV_PREFIX}python manage.py migrate
endif
.PHONY: install


.PHONY: clean
clean:  ## Remove all temporary files like pycache
	find . -name \*.rdb -type f -ls -delete
	find . -name \*.pyc -type f -ls -delete
	find . -name __pycache__ -ls -delete

# == Django Helpers
# ===================================================
djrun: install  ## Start Django server locally
	${ENV_PREFIX}python manage.py runserver


test: ARGS=--pdb --cov  ## Run all the tests
test: lint
	${ENV_PREFIX}pytest $(ARGS)

djmm:  ## Create Django migrations
	${ENV_PREFIX}python manage.py makemigrations

djmigrate:  # Run Django migrations
	${ENV_PREFIX}python manage.py migrate

djurls:  ## Displays all the django urls
	${ENV_PREFIX}python manage.py show_urls

shell:  ## Enter the django shell
	${ENV_PREFIX}python manage.py shell_plus

docs: virtualenv  ## Start documentation server locally
	${ENV_PREFIX}python -m pip install -r requirements/docs.txt
	${ENV_PREFIX}mkdocs serve

{%- if cookiecutter.add_celery == 'y' %}
celery: install  ## Start celery worker
	${ENV_PREFIX}celery -A $(PROJECT_NAME) worker -B -l INFO
{%- endif %}

redis:  ## Start redis server
	redis-server

# Ansible related things
# ------------------------------------------------------
# Usages:
# 	ENV=dev make configure
# 	ENV=dev make deploy
# 	ENV=dev make deploy_docs

run_ansible:
	@[ "${ENV}" ] || ( echo ">> ENV is not set"; exit 1 )
	${ENV_PREFIX}ansible-playbook -i $(INVENTORY) $(PLAYBOOK) --limit=$(ENV) $(ANSIBLE_ARGS)

configure: ANSIBLE_ARGS=--skip-tags=deploy
configure: run_ansible

deploy: ANSIBLE_ARGS=--tags=deploy
deploy: run_ansible

deploy_docs: ANSIBLE_ARGS=--tags=documentation  ## Deploy Documentation
deploy_docs: run_ansible

deploy_dev: ENV=dev  ## Deploy to Development Server
deploy_dev: deploy

deploy_qa: ENV=qa  ## Deploy to QA server
deploy_qa: deploy

deploy_prod: ENV=prod  ## Deploy to production server
deploy_prod: deploy
