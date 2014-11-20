# -*- coding: utf-8 -*-
'''Celery Worker Configuration to autodiscover tasks in all the django apps.

see: http://celery.readthedocs.org/en/latest/django/first-steps-with-django.html
'''
from __future__ import absolute_import

# Standard Library
import os
from os.path import dirname, join

# Third Party Stuff
from celery import Celery
from configurations import importer
from django.conf import settings

# SPECIAL RELATIVE IMPORT FIX FOR CELERY SETTINGS
from celery.schedules import crontab as crontab  # noqa


ROOT_DIR = dirname(dirname(__file__))

try:
    import dotenv
    dotenv.load_dotenv(join(ROOT_DIR, ".env"))
except ImportError:
    pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

importer.install()

app = Celery('{{ cookiecutter.repo_name }}-celery-app')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('%s:%s' % ('settings', os.environ.get('DJANGO_CONFIGURATION')))
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
