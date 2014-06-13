# -*- coding: utf-8 -*-
'''Fabric file for managing this project.

See: http://www.fabfile.org/
'''
from os.path import join, abspath, dirname

from fabric.api import local, env, lcd

ROOT = abspath(join(dirname(__file__)))

env.project = '{{ cookiecutter.repo_name }}'


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


def configure():
    local('npm install')


def serve_doc(address='127.0.0.1', port='8001'):
    with lcd(ROOT):
        local('mkdocs serve --dev-addr=%s:%s' % (address, port))


def manage(cmd):
    with lcd(ROOT):
        local('python {}/manage.py {}'.format(env.project, cmd))


def shell():
    manage('shell_plus')


def serve():
    manage('runserver_plus')


def syncdb():
    '''Synchronize database and generate changesets'''
    manage('syncdb --noinput')
    manage('migrate --noinput')


def makemigration(app):
    '''Generate a south migration for an application'''
    manage('schemamigration %s --auto' % app)
    manage('migrate %s --noinput' % app)
