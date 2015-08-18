from __future__ import absolute_import
import sh

from .base import DjangoCookieTestCase


class TestCookiecutterSubstitution(DjangoCookieTestCase):

    """Test that all cookiecutter instances are substituted"""

    def test_default_configuration(self):
        # Build a list containing absolute paths to the generated files
        self.generate_project()

    def test_flake8_compliance(self):
        self.generate_project()
        try:
            sh.flake8(self.destpath)
        except sh.ErrorReturnCode as e:
            raise AssertionError(e)
