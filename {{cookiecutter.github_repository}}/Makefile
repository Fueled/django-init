SHELL := bash
.ONESHELL:

PROJECT_NAME=insights
DB_NAME=$(PROJECT_NAME)
INVENTORY=provisioner/hosts
PLAYBOOK=provisioner/site.yml
PYTHON_PATH=venv/bin/

run:
# 	Run all these tasks in parallel, requires GNU Make
	make -j django docs celery redis

venv:
	virtualenv -p `which python3` venv

check:
	${PYTHON_PATH}black ${PROJECT_NAME} tests/ settings/
	${PYTHON_PATH}flake8 .

regenerate:
	-dropdb $(DB_NAME)
	createdb $(DB_NAME)
	${PYTHON_PATH}python manage.py migrate

install: venv
	${PYTHON_PATH}pip install -q -r requirements/development.txt
	${PYTHON_PATH}pre-commit install
ifneq ($(CI),True)
	-createdb $(DB_NAME)
	${PYTHON_PATH}python manage.py migrate
endif

clean:
	find . -name \*.rdb -type f -ls -delete
	find . -name \*.pyc -type f -ls -delete
	find . -name __pycache__ -ls -delete

django: install
	${PYTHON_PATH}python manage.py runserver

docs: install
	${PYTHON_PATH}mkdocs serve

celery: install
	${PYTHON_PATH}celery worker -A $(PROJECT_NAME) -B -l INFO

redis:
	redis-server

test: ARGS=--pdb --cov
test: check
	${PYTHON_PATH}pytest $(ARGS)

shell:
	${PYTHON_PATH}python manage.py shell_plus

# Ansible related things
# ------------------------------------------------------
# Usages:
# 	ENV=dev make configure
# 	ENV=dev make deploy
# 	ENV=dev make deploy_docs

run_ansible:
	@[ "${ENV}" ] || ( echo ">> ENV is not set"; exit 1 )
	${PYTHON_PATH}ansible-playbook -i $(INVENTORY) $(PLAYBOOK) --limit=$(ENV) $(ANSIBLE_ARGS)

configure: ANSIBLE_ARGS=--skip-tags=deploy
configure: run_ansible

deploy: ANSIBLE_ARGS=--tags=deploy
deploy: run_ansible

deploy_docs: ANSIBLE_ARGS=--tags=documentation
deploy_docs: run_ansible
