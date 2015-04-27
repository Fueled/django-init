# -*- coding: utf-8 -*-
''' Production Configurations

Adds sensible default for running app in production.
'''
from __future__ import absolute_import, unicode_literals

# Standard Library
from boto.s3.connection import OrdinaryCallingFormat



# Third Party Stuff
from configurations import values

from .common import Common


class Production(Common):

    INSTALLED_APPS = Common.INSTALLED_APPS

    # SITE CONFIGURATION
    # Hosts/domain names that are valid for this site.
    # "*" matches anything, ".example.com" matches example.com and all subdomains
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]

    INSTALLED_APPS += ("gunicorn", )

    # If your Django app is behind a proxy that sets a header to specify secure
    # connections, AND that proxy ensures that user-submitted headers with the
    # same name are ignored (so that people can't spoof it), set this value to
    # a tuple of (header_name, header_value). For any requests that come in with
    # that header/value, request.is_secure() will return True.
    # WARNING! Only set this if you fully understand what you're doing. Otherwise,
    # you may be opening yourself up to a security risk.
    # This ensures that Django will be able to detect a secure connection
    # properly on Heroku.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # django-secure
    # --------------------------------------------------------------------------
    INSTALLED_APPS += ("djangosecure", )

    MIDDLEWARE_CLASSES = (
        # Make sure djangosecure.middleware.SecurityMiddleware is listed first
        'djangosecure.middleware.SecurityMiddleware',
    )
    MIDDLEWARE_CLASSES += Common.MIDDLEWARE_CLASSES

    # set this to 60 seconds and then to 518400 when you can prove it works
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_FRAME_DENY = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SESSION_COOKIE_SECURE = values.BooleanValue(False)
    SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)

    # STORAGE CONFIGURATION
    # --------------------------------------------------------------------------
    # See: http://django-storages.readthedocs.org/en/latest/index.html
    INSTALLED_APPS += ('storages', )

    # See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
    try:
        from boto.s3.connection import OrdinaryCallingFormat
        AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()
    except ImportError:
        pass

    STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = values.SecretValue()
    AWS_SECRET_ACCESS_KEY = values.SecretValue()
    AWS_STORAGE_BUCKET_NAME = values.SecretValue()
    AWS_AUTO_CREATE_BUCKET = True
    AWS_QUERYSTRING_AUTH = False

    # see: https://github.com/antonagestam/collectfast
    AWS_PRELOAD_METADATA = True
    # For Django 1.7+, 'collectfast' should come before 'django.contrib.staticfiles'
    INSTALLED_APPS = ("collectfast", ) + INSTALLED_APPS

    # AWS cache settings, don't change unless you know what you're doing:
    AWS_EXPIREY = 60 * 60 * 24 * 7
    AWS_HEADERS = {
        'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (
            AWS_EXPIREY, AWS_EXPIREY)
    }

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME

    # EMAIL
    # --------------------------------------------------------------------------
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

    # CACHING
    # --------------------------------------------------------------------------
    redis_url = urlparse.urlparse(os.environ.get('REDISTOGO_URL', 'redis://localhost:6959'))

    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
            'OPTIONS': {
                'DB': 0,
                'PASSWORD': redis_url.password,
                'PARSER_CLASS': 'redis.connection.HiredisParser',
                'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
                'CONNECTION_POOL_CLASS_KWARGS': {
                    'max_connections': 50,
                    'timeout': 20,
                }
            }
        }
    }

    # TEMPLATE CONFIGURATION
    # --------------------------------------------------------------------------
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

    # Your production stuff: Below this line define 3rd party libary settings
