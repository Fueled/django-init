from __future__ import unicode_literals, absolute_import
# from configurations import values
from .development import Development


class Testing(Development):

    SKIP_SOUTH_TESTS = True
    SOUTH_TESTS_MIGRATE = False
    CELERY_ALWAYS_EAGER = True

    MEDIA_ROOT = "/tmp"

    SECRET_KEY = 'top-scret!'

    EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    INSTALLED_APPS = Development.INSTALLED_APPS + ("tests", )
