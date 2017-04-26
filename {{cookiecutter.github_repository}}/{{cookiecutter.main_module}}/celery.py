# -*- coding: utf-8 -*-

# Standard Library
import os

# Third Party Stuff
{%- if cookiecutter.use_sentry_for_error_reporting.lower() == 'y' %}
import raven
{%- endif %}
from celery import Celery
from django.conf import settings
from dotenv import load_dotenv
{%- if cookiecutter.use_sentry_for_error_reporting.lower() == 'y' %}
from raven.contrib.celery import register_logger_signal, register_signal
{%- endif %}

# set the default Django settings module for the 'celery' program.
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.development')
{%- if cookiecutter.use_sentry_for_error_reporting.lower() == 'y' %}


class CeleryCustomised(Celery):

    def on_configure(self):
        client = raven.Client(os.environ.get('SENTRY_DSN'), environment=os.environ.get('SENTRY_ENVIRONMENT'))

        # register a custom filter to filter out duplicate logs
        register_logger_signal(client)

        # hook into the Celery error handler
        register_signal(client)


app = CeleryCustomised('{{ cookiecutter.main_module }}')
{%- else %}


app = Celery('{{ cookiecutter.main_module }}')
{%- endif %}

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
