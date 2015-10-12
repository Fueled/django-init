from __future__ import absolute_import
import sh

from .base import DjangoCookieTestCase


class TestCookiecutterTemplating(DjangoCookieTestCase):
    """Test that all cookiecutter instances are substituted
    """

    def test_substitutions(self):
        paths = self.generate_project()
        self.check_paths(paths)

    def test_flake8_compliance(self):
        self.generate_project()
        try:
            sh.flake8(self.destpath)
        except sh.ErrorReturnCode as e:
            raise AssertionError(e)
