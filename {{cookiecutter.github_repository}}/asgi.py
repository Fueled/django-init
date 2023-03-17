# Standard Library
import os

# Third Party Stuff
from django.core.asgi import get_asgi_application
from dotenv import load_dotenv

# Read .env file and set key/value inside it as environement variables
# see: http://github.com/theskumar/python-dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.development'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.production")

application = get_asgi_application()
