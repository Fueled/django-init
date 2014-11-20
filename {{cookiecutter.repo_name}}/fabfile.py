# -*- coding: utf-8 -*-
'''Fabric file for managing this project.

See: http://www.fabfile.org/
'''
from __future__ import absolute_import, unicode_literals, with_statement

# Standard Library
import os
from contextlib import contextmanager as _contextmanager
from os.path import isdir, join

# Third Party Stuff
from fabric.api import cd, env, lcd, local, prefix, run, require

ROOT_DIR = os.getcwd()

# ==========================================================================
#  Settings
# ==========================================================================

env.project_name = '{{ cookiecutter.repo_name }}'
env.apps_dir = join(ROOT_DIR, env.project_name)
env.docs_dir = join(ROOT_DIR, 'docs')
env.virtualenv_dir = join(ROOT_DIR, 'venv')
env.dotenv_path = join(ROOT_DIR, '.env')
env.requirements_file = join(ROOT_DIR, 'requirements/development.txt')
env.shell = "/bin/bash -l -i -c"
env.use_ssh_config = True
env.config_setter = local

env.coverage_omit = '*tests*,*commands*,*migrations*,*admin*,*config*,*wsgi*'


#  Enviroments
# ---------------------------------------------------------
def prod():
    env.host_group = 'production'
    env.remote = 'origin'
    env.branch = 'prod'
    env.hosts = ['prod.{{ cookiecutter.repo_name }}.fueled.com']
    env.dotenv_path = '/home/ubuntu/{{ cookiecutter.github_reponame }}/.env'
    env.config_setter = run


def init(vagrant=False):
    '''Prepare a local machine for development.'''

    install_deps()
    config('set', 'DJANGO_SECRET_KEY', '`openssl rand -base64 32`')
    config('set', 'DATABASE_URL', 'postgres://localhost/%(project_name)s' % env)
    local('createdb %(project_name)s' % env)  # create postgres database
    manage('migrate')


def install_deps(file=env.requirements_file):
    '''Install project dependencies.'''
    verify_virtualenv()
    # activate virtualenv and install
    with virtualenv():
        local('pip install -r %s' % file)

    with cd(ROOT_DIR):
        local('npm install')


def serve_docs(address='127.0.0.1', port='8001'):
    '''Start a local server to view documentation changes.'''
    with lcd(ROOT_DIR):
        local('mkdocs serve --dev-addr=%s:%s' % (address, port))


def deploy_docs():
    with lcd(ROOT_DIR):
        local('mkdocs build')
        local('ghp-import -m "Documentaion updated." -p _docs_html')
        local('rm -rf _docs_html')


def shell():
    manage('shell_plus')


def test(options='--ipdb'):
    '''Run tests locally.'''
    with virtualenv():
        local('flake8 .')
        local("coverage run --source=onydo --omit='%s' -m py.test %s" % (env.coverage_omit, options))
        local("coverage report")


def webserver(host='127.0.0.1:8000'):
    '''Start an enhanced local app server'''
    install_deps()
    migrate()
    manage('runserver_plus %s' % host)


def serve():
    '''Start local webserver and documentation server with live-reload'''
    local('grunt serve')


def makemigrations(app=''):
    '''Create new database migration for an app.'''
    manage('makemigrations %s' % app)


def migrate():
    '''Apply database migrations.'''
    manage('migrate')


def createapp(appname):
    '''fab createapp <appname>
    '''
    path = join(env.apps_dir, appname)
    local('mkdir %s' % path)
    manage('startapp %s %s' % (appname, path))


def config(action=None, key=None, value=None):
    '''Manage project configuration using .env

    Usages: fab config:set,[key],[value]

    see: https://github.com/theskumar/python-dotenv
    '''
    command = 'dotenv'
    command += ' -f %(dotenv_path)s ' % env
    command += action + " " if action else " "
    command += key + " " if key else " "
    command += value if value else ""
    env.config_setter('touch %(dotenv_path)s' % env)

    with virtualenv():
        env.config_setter(command)


def configure():
    '''Setup a host using ansible scripts

    Usages: fab [prod|qa|dev] configure
    '''
    require('host_group')
    with lcd('provisioner'):
        local('ansible-playbook -v -i hosts site.yml --limit=%(host_group)s' % env)


# Helpers
# ---------------------------------------------------------
def manage(cmd, venv=True):
    with virtualenv():
        local('python manage.py %s' % cmd)


def create_graph_models():
    '''Generates graph of all the models in this project.'''
    graph_model_output = join(env.docs_dir, 'img/graph_model.svg')
    manage("graph_models -a -g -o %s" % graph_model_output)


@_contextmanager
def virtualenv():
    '''Activates virtualenv context for other commands to run inside it
    '''
    with cd(ROOT_DIR):
        with prefix('source %(virtualenv_dir)s/bin/activate' % env):
            yield


def verify_virtualenv():
    '''This modules check and install virtualenv if it not present.
    It also creates local virtualenv directory if it's not present
    '''
    from distutils import spawn
    if not spawn.find_executable('virtualenv'):
        local('sudo pip install virtualenv')

    if not isdir(env.virtualenv_dir):
        local('virtualenv %(virtualenv_dir)s' % env)
