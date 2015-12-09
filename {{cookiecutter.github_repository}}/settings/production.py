# -*- coding: utf-8 -*-
''' Production Configurations

Adds sensible default for running app in production.
- Disable DEBUG
- Make SECRET_KEY mandatory
- Use whitenoise to serve static files
'''
from __future__ import absolute_import, unicode_literals

from django.utils import six

from .common import *  # noqa


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANO_SECRET_KEY not in os.environ
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SITE CONFIGURATION
# Hosts/domain names that are valid for this site.
# "*" matches anything, ".example.com" matches example.com and all subdomains
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]

# DJANGO_SITES
# ------------------------------------------------------------------------------
# see: http://django-sites.readthedocs.org
SITES['remote'] = {
    "domain": env('SITE_DOMAIN'),
    "scheme": env('SITE_SCHEME', default='https'),
    "name": env('SITE_NAME'),
}
SITE_ID = env("DJANGO_SITE_ID", default='remote')

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
# ------------------------------------------------------------------------------
INSTALLED_APPS += ("djangosecure", )

MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'djangosecure.middleware.SecurityMiddleware',
) + MIDDLEWARE_CLASSES

# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
SECURE_FRAME_DENY = env.bool("DJANGO_SECURE_FRAME_DENY", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)


ENABLE_MEDIA_UPLOAD_TO_S3 = env.bool("ENABLE_MEDIA_UPLOAD_TO_S3", default=False)

# STORAGE CONFIGURATION
# ------------------------------------------------------------------------------
if ENABLE_MEDIA_UPLOAD_TO_S3:
    # Uploaded Media Files
    # ------------------------
    # See: http://django-storages.readthedocs.org/en/latest/index.html
    INSTALLED_APPS += (
        'storages',
    )
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')
    AWS_QUERYSTRING_AUTH = False

    # AWS cache settings, don't change unless you know what you're doing.
    AWS_EXPIRY = 60 * 60 * 24 * 7  # 1 week

    # TODO See: https://github.com/jschneier/django-storages/issues/47
    # Revert the following and use str after the above-mentioned bug is fixed in
    # either django-storage-redux or boto
    AWS_HEADERS = {
        'Cache-Control': six.b('max-age=%d, s-maxage=%d, must-revalidate' % (
            AWS_EXPIRY, AWS_EXPIRY))
    }

    # URL that handles the media served from MEDIA_ROOT, used for managing stored files.
    MEDIA_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME

# Static Assests
# ------------------------
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL',
                         default='{{ cookiecutter.project_name }} <{{ cookiecutter.django_admin_email }}>')
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_SUBJECT_PREFIX = env("EMAIL_SUBJECT_PREFIX", default='[{{cookiecutter.project_name}}] ')
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES['default'] = env.db("DATABASE_URL")

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "{0}{1}".format(env('REDISTOGO_URL', default="redis://localhost:6379/"), 0),
        'OPTIONS': {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            }
        }
    }
}

# https://docs.djangoproject.com/en/1.8/topics/http/sessions/#using-cached-sessions
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_CACHE_ALIAS = "default"

# TEMPLATE CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
]

# Your production stuff: Below this line define 3rd party libary settings
