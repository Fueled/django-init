#! env/python
from cookiecutter.main import cookiecutter
import sh


def generate_files():
    sh.rm('-rf', "djcookiecutter-test")
    ctx = {
        "repo_name": "djcookiecutter-test",
        "github_username": "Fueled",
        "github_reponame": "djcoookie",
        "project_name": "My Project",
        "project_description": "add a short project description here",
        "timezone": "UTC",
        "django_admin_email": "noreply@example.com",
        "version": "0.1.0",
        "domain_name": "subdomain.domain.com",
        "celery (y/n)": "n"
    }

    cookiecutter(input_dir='./', checkout=None, no_input=True, extra_context=ctx)


# test for jinja errors in rendering and any issue with hooks.
# It also prepares the files for subsequent testing via original test in rendered
# django project.

generate_files()
