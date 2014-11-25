{{ cookiecutter.project_name }}
==============================

![version {{ cookiecutter.version }}](http://img.shields.io/badge/Version-{{ cookiecutter.version }}-blue.svg)

{{ cookiecutter.project_description }}

## Getting up and running

Minimum requirements: **pip, fabric & postgres**, setup is tested on Mac OSX only.

In your terminal, type or copy-paste the following:
    
    git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_reponame }}.git; cd {{ cookiecutter.github_reponame }}; fab init

Go grab a cup of coffee, we bake your hot development machine.

Useful commands:

- `fab serve` - start [django server](http://localhost:8000/), [documentation server](http://localhost:8001/) and static file compiler
- `fab webserver` - run only webserver 
- `fab deploy_docs` - deploy docs to server
- `fab test` - run the test locally with ipdb

**NOTE:** Checkout `fabfile.py` for all the options available and what/how they do it.


## Deploying Project

The deployment are managed via travis, but for the first time you'll need to set the configuration values on each of the server.

Check out detailed server setup instruction [here](docs/backend/server_config.md).


## Contributing

Golden Rule:

> Anything in **master** is always **deployable**.

Avoid working on `master` branch, create a new branch with meaningful name, send pull request asap. Be vocal!

Refer to [CONTRIBUTING.md][contributing]

[contributing]: http://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_reponame}}/tree/master/CONTRIBUTING.md

--------
Built with ♥ at [Fueled](http://fueled.com)
