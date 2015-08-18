import os
import re
import shutil
import unittest
from os.path import exists, dirname, join

import sh

from cookiecutter.main import cookiecutter


class DjangoCookieTestCase(unittest.TestCase):

    root_dir = dirname(dirname(__file__))
    ctx = {}
    destpath = None

    def check_paths(self, paths):
        """
        Method to check all paths have correct substitutions,
        used by other tests cases
        """
        # Construct the cookiecutter search pattern
        pattern = "{{(\s?cookiecutter)[.](.*?)}}"
        re_obj = re.compile(pattern)

        # Assert that no match is found in any of the files
        for path in paths:
            for line in open(path, 'r'):
                match = re_obj.search(line)
                self.assertIsNone(
                    match,
                    "cookiecutter variable not replaced in {}".format(path))

    def generate_project(self, extra_context=None):
        ctx = {
            "repo_name": "djcookiecutter_fueled",
            "github_username": "Fueled",
            "github_reponame": "djcoookie",
            "project_name": "My Project",
            "project_description": "add a short project description here",
            "timezone": "UTC",
            "django_admin_email": "noreply@example.com",
            "version": "0.1.0",
            "celery (y/n)": "n"
        }
        if extra_context:
            assert isinstance(extra_context, dict)
            ctx.update(extra_context)

        self.ctx = ctx
        self.destpath = join(self.root_dir, self.ctx['repo_name'])

        cookiecutter(template='./', checkout=None, no_input=True, extra_context=ctx)

        # Build a list containing absolute paths to the generated files
        paths = [os.path.join(dirpath, file_path)
                 for dirpath, subdirs, files in os.walk(self.destpath)
                 for file_path in files]
        return paths

    def clean(self):
        if exists(self.destpath):
            shutil.rmtree(self.destpath)
        sh.cd(self.root_dir)

    def tearDown(self):
        self.clean()
