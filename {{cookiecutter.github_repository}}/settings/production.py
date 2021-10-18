"""Production Configurations

Adds sensible default for running app in production.
- Disable DEBUG
- Make SECRET_KEY mandatory
{%- if cookiecutter.enable_whitenoise.lower() == 'y' %}
- Use whitenoise to serve static files
{%- endif %}
- Disable browsable API
"""

# Standard Library
from email.utils import getaddresses

from .common import *  # noqa F405
from .common import (
    DATABASES,
    INSTALLED_APPS,
    {% if cookiecutter.add_django_auth_wall.lower() == 'y' %}MIDDLEWARE,{%- endif %}
    REST_FRAMEWORK,
    TEMPLATES,
    env,
)

# SITE CONFIGURATION
# Ensure these are set in the `.env` file manually.
SITE_SCHEME = env("SITE_SCHEME")
SITE_DOMAIN = env("SITE_DOMAIN")

# Hosts/domain names that are valid for this site.
# "*" matches anything, ".example.com" matches example.com and all subdomains
# See https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[SITE_DOMAIN])

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# People who get code error notifications.
# In the format "Full Name <email@example.com>, Full Name <anotheremail@example.com>"
ADMINS = getaddresses([env("DJANGO_ADMINS")])

# Not-necessarily-technical managers of the site. They get broken link
# notifications and other various emails.
MANAGERS = ADMINS

# CORS
# --------------------------------------------------------------------------
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")


{% if cookiecutter.add_django_auth_wall.lower() == "y" %}
# Basic Auth Protection
# -----------------------------------------------------------------------------
# see: https://github.com/theskumar/django-auth-wall#django-auth-wall
MIDDLEWARE = ["django_auth_wall.middleware.BasicAuthMiddleware"] + MIDDLEWARE
{%- endif %}

# If your Django app is behind a proxy that sets a header to specify secure
# connections, AND that proxy ensures that user-submitted headers with the
# same name are ignored (so that people can't spoof it), set this value to
# a tuple of (header_name, header_value). For any requests that come in with
# that header/value, request.is_secure() will return True.
# WARNING! Only set this if you fully understand what you"re doing. Otherwise,
# you may be opening yourself up to a security risk.
{%- if cookiecutter.enable_heroku_deployment.lower() == "y" %}
# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
{%- endif %}
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

#  SECURITY
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANGO_SECRET_KEY not in os.environ
SECRET_KEY = env("DJANGO_SECRET_KEY")

if SITE_SCHEME == "https":
    # set this to 60 seconds and then to 518400 when you can prove it works
    SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=60)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# STORAGE CONFIGURATION
# ------------------------------------------------------------------------------
ENABLE_MEDIA_UPLOAD_TO_S3 = env.bool("ENABLE_MEDIA_UPLOAD_TO_S3", default=False)
if ENABLE_MEDIA_UPLOAD_TO_S3:
    # Uploaded Media Files
    # ------------------------
    # See: http://django-storages.readthedocs.org/en/latest/index.html
    INSTALLED_APPS += [
        "storages",
    ]
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    AWS_ACCESS_KEY_ID = env("DJANGO_AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_HOST = env("DJANGO_AWS_S3_HOST", default="")
    AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)

    # AWS cache settings, don't change unless you know what you're doing.
    AWS_EXPIRY = 60 * 60 * 24 * 7  # 1 week

    # TODO See: https://github.com/jschneier/django-storages/issues/47
    # Revert the following and use str after the above-mentioned bug is fixed in
    # either django-storage-redux or boto
    AWS_HEADERS = {
        "Cache-Control": f"max-age={AWS_EXPIRY}, s-maxage={AWS_EXPIRY}, must-revalidate"
    }

    # URL that handles the media served from MEDIA_ROOT, used for managing stored files.
    MEDIA_URL = env(
        "MEDIA_URL", default="https://s3.amazonaws.com/%s/" % AWS_STORAGE_BUCKET_NAME
    )

# Static Assets
# ------------------------
{%- if cookiecutter.enable_whitenoise.lower() == "y" %}
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
{%- else %}
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
{%- endif %}

# EMAIL
# ------------------------------------------------------------------------------
# DEFAULT_FROM_EMAIL in settings/common.py
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES["default"].update(env.db("DATABASE_URL"))  # Don't override all db settings
{% if cookiecutter.postgis == "y" %}DATABASES["default"]["ENGINE"] = "django.contrib.gis.db.backends.postgis"{% endif %}

# CACHING
# ------------------------------------------------------------------------------
# Note: Specify different redis database name, if same redis instance is used.
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL", default="redis://localhost:6379/0"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PARSER_CLASS": "redis.connection.HiredisParser",
            "CONNECTION_POOL_CLASS": "redis.BlockingConnectionPool",
            "CONNECTION_POOL_CLASS_KWARGS": {
{%- if cookiecutter.enable_heroku_deployment.lower() == "y" %}
                # Hobby redistogo on heroku only supports max. 10, increase as required.
{%- endif %}
                "max_connections": env.int("REDIS_MAX_CONNECTIONS", default=10),
                "timeout": 20,
            },
        },
    }
}

# https://docs.djangoproject.com/en/1.10/topics/http/sessions/#using-cached-sessions
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_CACHE_ALIAS = "default"

# TEMPLATE CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]["OPTIONS"]["loaders"] = [
    ("django.template.loaders.cached.Loader", TEMPLATES[0]["OPTIONS"]["loaders"])
]

if not API_DEBUG:  # noqa: F405
    # blocking browsable api for rest framework and allowing just json renderer
    if (
        "rest_framework.renderers.BrowsableAPIRenderer"
        in REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"]
    ):
        REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"].remove(
            "rest_framework.renderers.BrowsableAPIRenderer"
        )
