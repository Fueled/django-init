# -*- coding: utf-8 -*-
"""Production Configurations

Adds sensible default for running app in production.
- Disable DEBUG
- Make SECRET_KEY mandatory
- Use whitenoise to serve static files
- Disable browsable API
"""

# Standard Library
from email.utils import getaddresses

# Third Party Stuff
from django.utils import six

from .common import *  # noqa: F405
from .common import DATABASES, INSTALLED_APPS, REST_FRAMEWORK, TEMPLATES, env

# SITE CONFIGURATION
# Hosts/domain names that are valid for this site.
# "*" matches anything, ".example.com" matches example.com and all subdomains
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]

SITE_SCHEME = env('SITE_SCHEME', default='https')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# People who get code error notifications.
# In the format 'Full Name <email@example.com>, Full Name <anotheremail@example.com>'
ADMINS = getaddresses([env("DJANGO_ADMINS")])

# Not-necessarily-technical managers of the site. They get broken link
# notifications and other various emails.
MANAGERS = ADMINS

# DJANGO_SITES
# ------------------------------------------------------------------------------
# see: http://niwinz.github.io/django-sites/latest/
SITES['remote'] = {  # noqa: F405
    "domain": env('SITE_DOMAIN'),
    "scheme": SITE_SCHEME,
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

#  SECURITY
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANO_SECRET_KEY not in os.environ
SECRET_KEY = env("DJANGO_SECRET_KEY")

if SITE_SCHEME == 'https':
    # set this to 60 seconds and then to 518400 when you can prove it works
    SECURE_HSTS_SECONDS = env.int('DJANGO_SECURE_HSTS_SECONDS', default=60)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# STORAGE CONFIGURATION
# ------------------------------------------------------------------------------
ENABLE_MEDIA_UPLOAD_TO_S3 = env.bool("ENABLE_MEDIA_UPLOAD_TO_S3", default=False)
if ENABLE_MEDIA_UPLOAD_TO_S3:
    # Uploaded Media Files
    # ------------------------
    # See: http://django-storages.readthedocs.org/en/latest/index.html
    INSTALLED_APPS += ('storages',)
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
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
{%- if cookiecutter.add_sass_with_django_compressor.lower() == 'y' %}

# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
COMPRESS_OFFLINE = True
{%- endif %}

# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL',
                         default='{{ cookiecutter.default_from_email }}')
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_SUBJECT_PREFIX = env("EMAIL_SUBJECT_PREFIX", default='[{{cookiecutter.project_name}}] ')
EMAIL_USE_TLS = True
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES['default'].update(env.db("DATABASE_URL"))  # Should not override all db settings
{% if cookiecutter.postgis == 'y' %}DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'{% endif %}

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env('REDIS_URL', default="redis://localhost:6379/"),
        'OPTIONS': {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                # Hobby redistogo on heroku only supports max. 10, increase as required.
                'max_connections': env.int('REDIS_MAX_CONNECTIONS', default=10),
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

if not API_DEBUG:  # noqa: F405
    # blocking browsable api for rest framework and allowing just json renderer
    if 'rest_framework.renderers.BrowsableAPIRenderer' in REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES']:
        REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].remove('rest_framework.renderers.BrowsableAPIRenderer')
