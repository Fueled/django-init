"""Development Settings

Adds sensible defaults for developement of project
- Enable DEBUG
- Log outgoing emails to console
- Enable Django Extensions
- Enable Django Debug Toolbar
- Use local caches
- Enable livereloading
"""

from .common import *  # noqa F405
from .common import INSTALLED_APPS, TEMPLATES, env

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool("DJANGO_DEBUG", default=True)
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # type: ignore

INTERNAL_IPS = ("127.0.0.1", "192.168.33.12")

ALLOWED_HOSTS = ["*"]

{%- if cookiecutter.enable_whitenoise.lower() == "y" %}
# Staticfiles
# ------------------------------------------------------------------------------
# Disable Django's static file handling and allow WhiteNoise to take over. This
# helps in minimizing dev/prod differences when serving static files.
INSTALLED_APPS = ["whitenoise.runserver_nostatic", ] + INSTALLED_APPS
{%- endif %}


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# A secret key for this particular Django installation. Used in secret-key
# hashing algorithms. Set this in your settings, or Django will complain
# loudly.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default="CHANGEME!!!")

# cors
# --------------------------------------------------------------------------
CORS_ALLOWED_ORIGINS = env.list(
    "CORS_ALLOWED_ORIGINS", default=["http://localhost", "http://localhost:8000"]
)

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405
INSTALLED_APPS += [
    "debug_toolbar",
]
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

# This will expose all browsable api urls. For dev the default value is true
API_DEBUG = env.bool("API_DEBUG", default=True)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

# Media configuration to support deployment of media files while is debug=True or development.
MEDIA_URL = env("MEDIA_URL", default="/media/")
