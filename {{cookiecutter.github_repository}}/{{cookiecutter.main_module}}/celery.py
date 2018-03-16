# Standard Library
import os

# Third Party Stuff
{%- if cookiecutter.use_sentry_for_error_reporting.lower() == 'y' %}
import raven
{%- endif %}
from celery import Celery
from django.conf import settings
from dotenv import load_dotenv

# Set the default Django settings module for the 'celery' program.
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.development')
{%- if cookiecutter.use_sentry_for_error_reporting.lower() == 'y' %}


class CeleryCustomised(Celery):

    def on_configure(self):
        client = raven.Client(os.getenv('SENTRY_DSN'), environment=os.getenv('SENTRY_ENVIRONMENT'))

        # register a custom filter to filter out duplicate logs
        raven.contrib.celery.register_logger_signal(client)

        # hook into the Celery error handler
        raven.contrib.celery.register_signal(client)


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

app.conf.beat_schedule = {}
