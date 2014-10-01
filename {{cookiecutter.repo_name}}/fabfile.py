# -*- coding: utf-8 -*-
'''Fabric file for managing this project.

See: http://www.fabfile.org/
'''
from __future__ import unicode_literals, absolute_import, with_statement
import os
from os.path import join, isdir
from fabric.api import local, env, lcd, cd, prefix
from contextlib import contextmanager as _contextmanager

here = os.getcwd()

env.project_name = '{{ cookiecutter.repo_name }}'
env.apps_dir = join(here, env.project_name)
env.virtualenv_dir = join(here, 'venv')
env.dotenv_path = join(env.apps_dir, '.env')
env.requirements_file = join(here, 'configurations/pip/development.txt')
env.shell = "/bin/bash -l -i -c"


def init(vagrant=False):
    '''Prepare a local machine for development.'''

    install_deps()
    local('createdb %(project_name)s' % env)  # create postgres database
    config('set', 'DJANGO_SECRET_KEY', '`openssl rand -base64 32`')
    config('set', 'DATABASE_URL', 'postgres://localhost/%(project_name)s' % env)
    manage('migrate')


def install_deps(file=env.requirements_file):
    '''Install project dependencies.'''
    verify_virtualenv()
    # activate virtualenv and install
    with virtualenv():
        local('pip install -r %s' % file)

    with cd(here):
        local('npm install')


def serve_doc(address='127.0.0.1', port='8001'):
    with lcd(here):
        local('mkdocs serve --dev-addr=%s:%s' % (address, port))


def shell():
    manage('shell_plus')


def serve(host='127.0.0.1:8000'):
    '''Start an enhanced runserver'''
    install_deps()
    migrate()
    manage('runserver_plus %s' % host)


def migrate():
    '''Synchronize database and generate changesets'''
    manage('migrate')


def createapp(appname):
    '''fab createapp <appname>
    '''
    path = join(env.apps_dir, appname)
    local('mkdir %s' % path)
    manage('startapp %s %s' % (appname, path))


def makemigrations(app):
    '''Generate a south migration for an application'''
    manage('makemigrations')


def config(action=None, key=None, value=None):
    '''Manage project configuration via .env

    see: https://github.com/theskumar/python-dotenv
    e.g: fab config:set,[key],[value]
    '''
    command = 'dotenv'
    command += ' -f %s ' % env.dotenv_path
    command += action + " " if action else " "
    command += key + " " if key else " "
    command += value if value else ""
    local('touch %(dotenv_path)s' % env)

    with virtualenv():
        local(command)


# Helpers
# ------------------------------------------------------------------------------
def manage(cmd, venv=True):
    with virtualenv():
        local('python {project}/manage.py %s' % (env.project_name, cmd))


@_contextmanager
def virtualenv():
    '''Activates virtualenv context for other commands to run inside it
    '''
    with cd(here):
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
