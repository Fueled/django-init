"""Django settings for {{cookiecutter.project_name}} project.

see: https://docs.djangoproject.com/en/dev/ref/settings/
"""
# Third Party Stuff
import environ
from corsheaders.defaults import default_headers
from django.utils.translation import gettext_lazy as _

ROOT_DIR = environ.Path(__file__) - 2  # (/a/b/myfile.py - 2 = /a/)
APPS_DIR = ROOT_DIR.path("{{ cookiecutter.main_module }}")

env = environ.Env()

# INSTALLED APPS
# ==========================================================================
# List of strings representing installed apps.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.postgres",
    "django_sites",  # http://niwinz.github.io/django-sites/latest/
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
]

THIRD_PARTY_APPS = [
    "django_filters",
    "rest_framework",  # http://www.django-rest-framework.org/
{%- if cookiecutter.add_graphql == "y" %}
    "graphene_django",
{%- endif %}
    "mail_templated",  # https://github.com/artemrizhov/django-mail-templated
    "django_extensions",  # http://django-extensions.readthedocs.org/
    "drf_yasg",
    "versatileimagefield",  # https://github.com/WGBH/django-versatileimagefield/
    "corsheaders",  # https://github.com/ottoyiu/django-cors-headers/
{%- if cookiecutter.add_sentry == "y" %}
    "raven.contrib.django.raven_compat",
{%- endif %}
]

LOCAL_APPS = [
    "{{ cookiecutter.main_module }}.base",
    "{{ cookiecutter.main_module }}.users",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# INSTALLED APPS CONFIGURATION
# ==========================================================================

# django.contrib.auth
# ------------------------------------------------------------------------------
AUTH_USER_MODEL = "users.User"
AUTHENTICATION_BACKENDS = [
{%- if cookiecutter.add_graphql == "y" %}
    "graphql_jwt.backends.JSONWebTokenBackend",
{%- endif %}
    "django.contrib.auth.backends.ModelBackend",
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 6},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# For Exposing browsable api urls. By default urls won't be exposed.
API_DEBUG = env.bool("API_DEBUG", default=False)

# rest_framework
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
{%- if cookiecutter.pagination == 'CursorPagination' %}
    # Cursor Pagination require ordering on field `-created_at`. Make sure that field is part of each model
    # Cursor Pagination does not returns the `count` as part of the response
{%- endif %}
    "DEFAULT_PAGINATION_CLASS": "{{ cookiecutter.main_module }}.base.api.pagination.{{ cookiecutter.pagination }}",
    "PAGE_SIZE": 30,
    # Default renderer classes for Rest framework
    "DEFAULT_RENDERER_CLASSES": [
        "{{ cookiecutter.main_module }}.base.renderers.{{ cookiecutter.main_module|replace('_', ' ')|replace('-', ' ')|title|replace(' ', '') }}ApiRenderer",
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    # "Accept" header based versioning
    # http://www.django-rest-framework.org/api-guide/versioning/
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.AcceptHeaderVersioning",
    "DEFAULT_VERSION": "1.0",
    "ALLOWED_VERSIONS": ["1.0"],
    "VERSION_PARAMETER": "version",
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_THROTTLE_CLASSES": ["rest_framework.throttling.AnonRateThrottle"],
    "DEFAULT_THROTTLE_RATES": {"anon": "10000/day"},
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        # Primary api authentication
        "{{ cookiecutter.main_module }}.users.auth.backends.UserTokenAuthentication",
        # Mainly used for api debug.
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "EXCEPTION_HANDLER": "{{ cookiecutter.main_module }}.base.exceptions.exception_handler",
}

{%- if cookiecutter.add_graphql == "y" %}
GRAPHENE = {
    # The location of the top-level Schema class.
    "SCHEMA": "{{ cookiecutter.main_module }}.graphql.api.schema",

    # The maximum size of objects that can be requested through a relay connection.
    "RELAY_CONNECTION_MAX_LIMIT": 100,
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}

GRAPHQL_JWT = {
    "JWT_PAYLOAD_GET_USERNAME_HANDLER": (
        lambda payload: payload.get('user_authentication_id')
    ),
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    "JWT_GET_USER_BY_NATURAL_KEY_HANDLER": "{{ cookiecutter.main_module }}.users.services.get_active_user_by_id",
}
{%- endif %}

# https://django-rest-swagger.readthedocs.io/en/latest/settings/
SWAGGER_SETTINGS = {
    "LOGIN_URL": "rest_framework:login",
    "LOGOUT_URL": "rest_framework:logout",
    "SECURITY_DEFINITIONS": {
        # For BasicAuthentication
        "basic": {"type": "basic"},
        # For UserTokenAuthentication
        "api_key": {"type": "apiKey", "name": "Authorization", "in": "header"},
    },
}

# DJANGO_SITES
# ------------------------------------------------------------------------------
# see: http://django-sites.readthedocs.org
SITE_SCHEME = env("SITE_SCHEME", default="http")
SITE_DOMAIN = env("SITE_DOMAIN", default="localhost:8000")
SITE_NAME = env("SITE_NAME", default="{{ cookiecutter.project_name }}")

# This is used in-case of the frontend is deployed at a different url than this django app.
FRONTEND_SITE_SCHEME = env("FRONTEND_SITE_SCHEME", default="https")
FRONTEND_SITE_DOMAIN = env("FRONTEND_SITE_DOMAIN", default="example.com")
FRONTEND_SITE_NAME = env("FRONTEND_SITE_NAME", default="{{ cookiecutter.project_name }}")

SITES = {
    "current": {"domain": SITE_DOMAIN, "scheme": SITE_SCHEME, "name": SITE_NAME},
    "frontend": {
        "domain": FRONTEND_SITE_DOMAIN,
        "scheme": FRONTEND_SITE_SCHEME,
        "name": FRONTEND_SITE_NAME,
    },
}
SITE_ID = "current"

# see user.services.send_password_reset
# password-confirm path should have placeholder for token
FRONTEND_URLS = {
    "home": "/",
    "password-confirm": "/reset-password/{token}/",
}

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
# List of middleware classes to use.  Order is important; in the request phase,
# this middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "log_request_id.middleware.RequestIDMiddleware",  # For generating/adding Request id for all the logs
    "django.middleware.security.SecurityMiddleware",
{%- if cookiecutter.enable_whitenoise.lower() == "y" %}
    "whitenoise.middleware.WhiteNoiseMiddleware",
{%- endif %}
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# DJANGO CORE
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
# Defaults to false, which is safe, enable them only in development.
DEBUG = env.bool("DJANGO_DEBUG", False)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = "{{ cookiecutter.timezone }}"

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

# Languages we provide translations for
LANGUAGES = (("en", _("English")),)

if USE_TZ:
    # Add timezone information to datetime displayed.
    # https://mounirmesselmeni.github.io/2014/11/06/date-format-in-django-admin/
    from django.conf.locale.en import formats as en_formats

    en_formats.DATETIME_FORMAT = "N j, Y, P (e)"

# A tuple of directories where Django looks for translation files.
LOCALE_PATHS = (str(APPS_DIR.path("locale")),)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# The list of directories to search for fixtures
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (str(APPS_DIR.path("fixtures")),)

# The Python dotted path to the WSGI application that Django's internal servers
# (runserver, runfcgi) will use. If `None`, the return value of
# "django.core.wsgi.get_wsgi_application" is used, thus preserving the same
# behavior as previous versions of Django. Otherwise this should point to an
# actual WSGI application object.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "wsgi.application"

# URL CONFIGURATION
# ------------------------------------------------------------------------------
ROOT_URLCONF = "{{ cookiecutter.main_module }}.urls"


# Use this to change base url path django admin
DJANGO_ADMIN_URL = env.str("DJANGO_ADMIN_URL", default="admin")

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
DEFAULT_FROM_EMAIL = env(
    "DEFAULT_FROM_EMAIL", default="{{ cookiecutter.default_from_email }}"
)
EMAIL_SUBJECT_PREFIX = env("EMAIL_SUBJECT_PREFIX", default="[{{cookiecutter.project_name}}] ")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
SERVER_EMAIL = env("SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# Using unix socket for postgres connection by default
DATABASES = {"default": env.db("DATABASE_URL", default="postgres:///{{ cookiecutter.main_module }}")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = 10
{% if cookiecutter.add_postgis.lower() == "y" %}DATABASES["default"]["ENGINE"] = "django.contrib.gis.db.backends.postgis"{% endif %}

# TEMPLATE CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR.path("templates"))],
        "OPTIONS": {
            "debug": DEBUG,
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "{{cookiecutter.main_module}}.base.context_processors.site_settings",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
                # Your stuff: custom template context processors go here
            ],
        },
    }
]

CSRF_FAILURE_VIEW = "{{ cookiecutter.main_module }}.base.views.csrf_failure"

# STATIC FILE CONFIGURATION
# -----------------------------------------------------------------------------
# Absolute path to the directory static files should be collected to.
# Example: "/var/www/example.com/static/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR.path(".staticfiles"))

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://example.com/static/", "http://static.example.com/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# A list of locations of additional static files
STATICFILES_DIRS = (str(APPS_DIR.path("static")),)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR.path(".media"))

# URL that handles the media served from MEDIA_ROOT.
# Examples: "http://example.com/media/", "http://media.example.com/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = env("MEDIA_URL", default="{}://{}/media/".format(SITE_SCHEME, SITE_DOMAIN))

#  SECURITY
# -----------------------------------------------------------------------------
CSRF_COOKIE_HTTPONLY = False  # Allow javascripts to read CSRF token from cookies
SESSION_COOKIE_HTTPONLY = True  # Do not allow Session cookies to be read by javascript

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# django-log-request-id - Sending request id in response
REQUEST_ID_RESPONSE_HEADER = "REQUEST_ID"

# CORS
# --------------------------------------------------------------------------
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_HEADERS = default_headers + ("access-control-allow-origin",)


{%- if cookiecutter.add_celery.lower() == "y" %}

# DJANGO CELERY CONFIGURATION
# -----------------------------------------------------------------------------
# see: http://celery.readthedocs.org/en/latest/userguide/tasks.html#task-states
CELERY_BROKER_URL = env("REDIS_URL", default="redis://localhost:6379/0")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = env(
    "CELERY_TIMEZONE", default=TIME_ZONE
)  # Use Django's timezone by default
{%- endif %}

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# Default logging for Django. This sends an email to the site admins on every
# HTTP 500 error. Depending on DEBUG, all other log records are either sent to
# the console (DEBUG=True) or discarded by mean of the NullHandler (DEBUG=False).
# See http://docs.djangoproject.com/en/dev/topics/logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
        "request_id": {"()": "log_request_id.filters.RequestIDFilter"},
    },
    "formatters": {
        "complete": {
            # NOTE: make sure to include "request_id" in filters when using this
            # formatter in any handlers.
            "format": "%(asctime)s:[%(levelname)s]:logger=%(name)s:request_id=%(request_id)s message='%(message)s'"
        },
        "simple": {"format": "%(levelname)s:%(asctime)s: %(message)s"},
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[%(server_time)s] %(message)s",
        },
    },
    "handlers": {
        "null": {"level": "DEBUG", "class": "logging.NullHandler"},
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "complete",
            "filters": ["request_id"],
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        {%- if cookiecutter.add_sentry == "y" %}
        "sentry": {
            "level": "ERROR",
            "class": "raven.contrib.django.raven_compat.handlers.SentryHandler",
            "formatter": "complete",
            "filters": ["request_id"],
        },
        {%- endif %}
    },
    "loggers": {
        "django": {"handlers": ["null"], "propagate": False, "level": "INFO"},
        "django.request": {
            "handlers": ["mail_admins", "console"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
        "{{cookiecutter.main_module}}": {"handlers": ["console"], "level": "INFO", "propagate": False},
        # Catch All Logger -- Captures any other logging
        "": {"handlers": ["console",{%- if cookiecutter.add_sentry == "y" %} "sentry"{%- endif %}], "level": "ERROR", "propagate": True},
    },
}


def get_release():
    {%- if cookiecutter.add_sentry == "y" %}
    import os

    import raven
{% endif %}
    import {{cookiecutter.main_module}}

    release = {{cookiecutter.main_module}}.__version__
    {%- if cookiecutter.add_sentry == "y" %}
    try:
        git_hash = raven.fetch_git_sha(os.path.dirname(os.pardir))[:7]
        release = "{}-{}".format(release, git_hash)
    except raven.exceptions.InvalidGitRepository:
        pass
    {%- endif %}
    return release


RELEASE_VERSION = get_release()


{%- if cookiecutter.add_sentry == "y" %}
RAVEN_CONFIG = {
    "dsn": env("SENTRY_DSN", default=""),
    "environment": env("SENTRY_ENVIRONMENT", default="production"),
    "release": RELEASE_VERSION,
}
{%- endif %}

SITE_INFO = {
    "RELEASE_VERSION": RELEASE_VERSION,
{%- if cookiecutter.add_sentry == "y" %}
    "IS_RAVEN_INSTALLED": True if RAVEN_CONFIG.get("dsn") else False,
{%- endif %}
}
