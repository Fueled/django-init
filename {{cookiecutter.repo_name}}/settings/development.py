# -*- coding: utf-8 -*-
''' Development Configurations

Adds sensible defaults for developement of project
- Enables DEBUG
- Outputs outgoing emails to console
- Enables Django Debug Toolbar
- Uses local caches
- override SITE_ID to use 'local'
'''
from __future__ import unicode_literals, absolute_import
from configurations import values
from .common import Common


class Development(Common):

    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = DEBUG

    INSTALLED_APPS = Common.INSTALLED_APPS

    # EMAIL
    # --------------------------------------------------------------------------
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')

    # CACHES
    # --------------------------------------------------------------------------
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': ''
        }
    }

    # DJANGO_SITES
    # --------------------------------------------------------------------------
    SITE_ID = 'local'

    # django-debug-toolbar
    # --------------------------------------------------------------------------
    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)

    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': ['debug_toolbar.panels.redirects.RedirectsPanel', ],
        'SHOW_TEMPLATE_CONTEXT': True,
    }

    # PUSH NOTIFICATION CONFIG
    # -------------------------------------------------------------------------
    DISABLE_PUSH_NOTIFICATION = values.BooleanValue(True)
