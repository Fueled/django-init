'''Fabric file for managing this project.'''
from fabric.api import local, env


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
    local('mkdocs serve --dev-addr=%s:%s' % (address, port))


def manage(cmd):
    local('python {{ cookiecutter.repo_name}}/manage.py {}'.format(cmd))


def shell():
    manage('shell_plus')


def serve():
    manage('runserver')
