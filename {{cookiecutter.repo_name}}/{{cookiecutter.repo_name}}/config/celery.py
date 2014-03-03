# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

settings_module = 'config.settings'
configuration_module = 'Local'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
os.environ.setdefault('DJANGO_CONFIGURATION', configuration_module)

from configurations import importer
importer.install()

app = Celery('{{ cookiecutter.repo_name }}')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('%s:%s' % settings_module, configuration_module)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
