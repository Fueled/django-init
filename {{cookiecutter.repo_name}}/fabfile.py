# -*- coding: utf-8 -*-
'''Fabric file for managing this project.

See: http://www.fabfile.org/
'''
from os.path import join, abspath, dirname

from fabric.api import local, env, lcd

PROJECT_ROOT = abspath(join(dirname(__file__)))

env.project = '{{ cookiecutter.repo_name }}'
env.apps_dir = join(PROJECT_ROOT, env.project)


def init(vagrant=True):
    '''Prepare a local machine for development.'''

    distro = local('uname -s', capture=True)

    if distro == 'Darwin':  # OSX
        env.installer = 'brew cask install'
    elif distro == 'Linux':
        env.installer = 'sudo apt-get install'
    else:
        print "Error: Your operating system (%s) is not supported yet" % distro
    if vagrant:
        local('%(installer)s virtualbox vagrant' % env)
        local('vagrant plugin install vagrant-vbguest')
    local('sudo pip install ansible')
    config('set','DJANGO_SECRET_KEY','`openssl rand -base64 32`')


def configure():
    local('npm install')


def serve_doc(address='127.0.0.1', port='8001'):
    with lcd(PROJECT_ROOT):
        local('mkdocs serve --dev-addr=%s:%s' % (address, port))


def manage(cmd):
    with lcd(PROJECT_ROOT):
        local('python {}/manage.py {}'.format(env.project, cmd))


def shell():
    manage('shell_plus')


def serve():
    manage('runserver_plus')


def syncdb():
    '''Synchronize database and generate changesets'''
    manage('syncdb --noinput')
    manage('migrate --noinput')


def startapp(appname):
    '''fab startapp <appname>
    '''
    path = join(env.apps_dir, appname)
    local('mkdir %s' % path)
    manage('startapp %s %s' % (appname, path))


def makemigration(app):
    '''Generate a south migration for an application'''
    manage('schemamigration %s --auto' % app)
    manage('migrate %s --noinput' % app)


def config(action=None,key=None,value=None):
    '''
    Overwrites the .env file and set custom ENV variables
    ref: https://github.com/tedtieken/django-dotenv-rw
    example usage: fab config:set,[key],[value]
    '''
    command = env.project + "/dotenv.py "
    command += env.project + "/.env "
    command += action + " " if action else ""
    command += key + " " if key else ""
    command += value + " " if value else ""
    local('python {}'.format(command))
