# -*- coding: utf-8 -*-
'''Fabric file for managing this project.

See: http://www.fabfile.org/
'''
from os.path import join, abspath, dirname
from fabric.api import local, env, lcd

here = abspath(join(dirname(__file__)))

env.project = '{{ cookiecutter.repo_name }}'
env.apps_dir = join(here, env.project)
env.dotenv_path = join(env.apps_dir, '.env')
env.requirements_file = join(here, 'configuration/pip/development.txt')


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
    config('set', 'DJANGO_SECRET_KEY', '`openssl rand -base64 32`')


def install_deps():
    '''Install project dependencies.'''
    local('npm install')
    local('pip install -r %(requirements_file)s' % env)


def serve_doc(address='127.0.0.1', port='8001'):
    with lcd(here):
        local('mkdocs serve --dev-addr=%s:%s' % (address, port))


def manage(cmd):
    with lcd(here):
        local('python {}/manage.py {}'.format(env.project, cmd))


def shell():
    manage('shell_plus')


def serve(host='127.0.0.1:8000'):
    '''Start an enhanced runserver'''
    install_deps()
    manage('runserver_plus %s' % host)


def migrate():
    '''Synchronize database and generate changesets'''
    manage('migrate')


def startapp(appname):
    '''fab startapp <appname>
    '''
    path = join(env.apps_dir, appname)
    local('mkdir %s' % path)
    manage('startapp %s %s' % (appname, path))


def makemigrations(app):
    '''Generate a south migration for an application'''
    manage('makemigrations')


def config(action=None, key=None, value=None):
    '''
    Overwrites the .env file and set custom ENV variables
    ref: https://github.com/theskumar/python-dotenv
    example usage: fab config:set,[key],[value]
    '''
    local('touch %(dotenv_path)s' % env)
    command = 'dotenv'
    command += ' -f %s' % env.dotenv_path
    command += action if action else " "
    command += key if key else " "
    command += value if value else ""
    local(command)
