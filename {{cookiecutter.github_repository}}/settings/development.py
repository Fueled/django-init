# -*- coding: utf-8 -*-
"""Development Settings

Adds sensible defaults for developement of project
- Enable DEBUG
- Log outgoing emails to console
- Enable Django Extensions
- Enable Django Debug Toolbar
- Use local caches
- Enable livereloading
"""
from __future__ import absolute_import, unicode_literals

from .common import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

INTERNAL_IPS = ('127.0.0.1', )

# Staticfiles
# ------------------------------------------------------------------------------
# Disable Django's static file handling and allow WhiteNoise to take over. This
# helps in minimizing dev/prod differences when serving static files.
INSTALLED_APPS = ('whitenoise.runserver_nostatic', ) + INSTALLED_APPS

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# A secret key for this particular Django installation. Used in secret-key
# hashing algorithms. Set this in your settings, or Django will complain
# loudly.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!')

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-extensions (http://django-extensions.readthedocs.org/)
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )

# LiveReload Support with devrecargar
# ------------------------------------------------------------------------------
# https://github.com/scottwoodall/django-devrecargar
INSTALLED_APPS += ('devrecargar',)

DEVRECARGAR_PATHS_TO_WATCH = [{
    'path': str(APPS_DIR),
    'patterns': ['*.html', '*.js', '*.css', '*.scss'],
}]

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': ['debug_toolbar.panels.redirects.RedirectsPanel', ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# This will expose all browsable api urls. For dev the default value is true
API_DEBUG = env.bool('API_DEBUG', default=True)
