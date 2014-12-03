# -*- coding: utf-8 -*-
''' Production Configurations

Adds sensible default for running app in production.
'''
from __future__ import unicode_literals, absolute_import
from configurations import values
from .common import Common


class Production(Common):

    # This ensures that Django will be able to detect a secure connection
    # properly on Heroku.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # django-secure
    INSTALLED_APPS += ("djangosecure", )

    # set this to 60 seconds and then to 518400 when you can prove it works
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_FRAME_DENY = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SESSION_COOKIE_SECURE = values.BooleanValue(False)
    SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    # end django-secure

    # SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    # END SITE CONFIGURATION

    INSTALLED_APPS += ("gunicorn", )

    # STORAGE CONFIGURATION
    # See: http://django-storages.readthedocs.org/en/latest/index.html
    INSTALLED_APPS += ('storages', )

    # See:
    # http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
    try:
        from boto.s3.connection import OrdinaryCallingFormat
        AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()
    except ImportError:
        pass

    STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = values.SecretValue(
        environ=True, environ_name='AWS_ACCESS_KEY_ID', environ_prefix='DJANGO')
    AWS_SECRET_ACCESS_KEY = values.SecretValue(
        environ=True, environ_name='AWS_SECRET_ACCESS_KEY', environ_prefix='DJANGO')
    AWS_STORAGE_BUCKET_NAME = values.SecretValue(
        environ=True, environ_name='AWS_STORAGE_BUCKET_NAME', environ_prefix='DJANGO')
    AWS_AUTO_CREATE_BUCKET = True
    AWS_QUERYSTRING_AUTH = False

    # see: https://github.com/antonagestam/collectfast
    AWS_PRELOAD_METADATA = True
    INSTALLED_APPS += ("collectfast", )

    # AWS cache settings, don't change unless you know what you're doing:
    AWS_EXPIREY = 60 * 60 * 24 * 7
    AWS_HEADERS = {
        'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (
            AWS_EXPIREY, AWS_EXPIREY)
    }

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
    # END STORAGE CONFIGURATION

    # Email
    DEFAULT_FROM_EMAIL = values.Value(
        '{{ cookiecutter.project_name }} <{{ cookiecutter.django_admin_email }}>')
    EMAIL_HOST = values.Value('smtp.sendgrid.com')
    EMAIL_HOST_PASSWORD = values.SecretValue(environ_prefix="", environ_name="SENDGRID_PASSWORD")
    EMAIL_HOST_USER = values.SecretValue(environ_prefix="", environ_name="SENDGRID_USERNAME")
    EMAIL_PORT = values.IntegerValue(587, environ_prefix="", environ_name="EMAIL_PORT")
    EMAIL_SUBJECT_PREFIX = values.Value('[{{ cookiecutter.project_name }}] ', environ_name="EMAIL_SUBJECT_PREFIX")
    EMAIL_USE_TLS = True
    SERVER_EMAIL = DEFAULT_FROM_EMAIL
    # END EMAIL

    try:
        # see: https://github.com/rdegges/django-heroku-memcacheify#install
        # Avoids installing of pylibmc on development enviroment
        from memcacheify import memcacheify
        CACHES = memcacheify()
    except ImportError:
        CACHES = values.CacheURLValue(default="memcached://127.0.0.1:11211")

    # TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
    # END TEMPLATE CONFIGURATION

    # Your production stuff: Below this line define 3rd party libary settings
