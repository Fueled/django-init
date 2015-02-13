# -*- coding: utf-8 -*-
# Standard Library
import os

# Third Party Stuff
import django
import pytest

from .fixtures import *  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Development")


def pytest_addoption(parser):
    parser.addoption("--runslow", action="store_true", help="run slow tests")


def pytest_runtest_setup(item):
    if "slow" in item.keywords and not item.config.getoption("--runslow"):
        pytest.skip("need --runslow option to run")


def pytest_configure(config):
    django.setup()
