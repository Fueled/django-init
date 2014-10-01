# -*- coding: utf-8 -*-
'''Celery Worker Configuration to autodiscover tasks in all the django apps.

see: http://celery.readthedocs.org/en/latest/django/first-steps-with-django.html
'''
from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

_SETTINGS_MODULE = 'config.development'
_CONFIGURATION_MODULE = 'Development'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', _SETTINGS_MODULE)
os.environ.setdefault('DJANGO_CONFIGURATION', _CONFIGURATION_MODULE)

from configurations import importer
importer.install()

app = Celery('{{ cookiecutter.repo_name }}')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('%s:%s' % (_SETTINGS_MODULE, _CONFIGURATION_MODULE))
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
