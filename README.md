cookiecutter-django
====================

Project template for django based projects.

## Features

* Django 1.7+
* PostresSQL 9.3
* Foundation 5.4.7
* SASS, CoffeeScript, Live-Reloading Server
* Ansible script for deploying to EC2/Ubuntu
* Heroku/Sendgrid/S3
* [12factor][12factor] based project configuration
* Django Rest Framework 3.0+
* `django_sites` instead of `django.contrib.sites`

[mkdocs]: http://www.mkdocs.org/
[12factor]: http://12factor.net

## Getting Started

Following are system level dependecies, and must be present on your machine before you run cookiecutter command. Primarily for `pre_gen_project.sh` to complete successfully.

- **postgres** - can be installed with `brew install postgres`
- **sass** - can be installed with `gem install sass`
- **graphviz** - can be installed with `brew install graphviz`
- **fabric** - can be installed with `sudo pip install fabric`

You should able to install these fairly easily if your developement machine is other than a Mac OS X.

You need to have `cookiecutter` installed in order to scafold a new project from this template. If you have `pip` installed, you simply do this by running:

    pip install --upgrade cookiecutter

After the installation is successful, you can create a new django project by simply running:

    cookiecutter https://github.com/Fueled/cookiecutter-django.git

It will ask you to some questions, after which it will create a new project in your current working directory. It will also create a virtualenv in the folder `venv` inside the project, and install all the python dependencies inside it.

Once the cookiecutter is finishes, you'll have:

1. A postgres database created, with name same as `repo_name` you provided.
2. Installed all the npm packages required
3. Installed all the python dependencies in virtualenv
4. Local settings added to `.env` file (untracked)
5. Initialized a git repo and created the first commit.

Now the only thing you'll need to do is:

1. `cd` into the new `repo_name` folder
2. Run `fab serve`

Read the instructions in `README.md`, inside the project to get much detailed instructions.

--------

Built with ♥ at [Fueled](http://fueled.com)
