# Standard Library
import os

# Third Party Stuff
from celery import Celery
from django.conf import settings
from dotenv import load_dotenv

# set the default Django settings module for the 'celery' program.
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.development')


app = Celery('{{ cookiecutter.main_module }}')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
