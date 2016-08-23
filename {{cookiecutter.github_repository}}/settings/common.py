# -*- coding: utf-8 -*-
"""Django settings for {{cookiecutter.project_name}} project.

see: https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Third Party Stuff
import environ
from django.utils.translation import ugettext_lazy as _

ROOT_DIR = environ.Path(__file__) - 2  # (/a/b/myfile.py - 2 = /a/)
APPS_DIR = ROOT_DIR.path('{{ cookiecutter.main_module }}')

env = environ.Env()

# INSTALLED APPS
# ==========================================================================
# List of strings representing installed apps.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django_sites',  # http://niwinz.github.io/django-sites/latest/
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # 'django.contrib.humanize',  # Useful template tags

    '{{ cookiecutter.main_module }}.base',
    '{{ cookiecutter.main_module }}.users',

    'rest_framework',  # http://www.django-rest-framework.org/
    'versatileimagefield',  # https://github.com/WGBH/django-versatileimagefield/
{%- if cookiecutter.add_sass_with_django_compressor.lower() == 'y' %}

    'compressor',
{%- endif %}
)

# INSTALLED APPS CONFIGURATION
# ==========================================================================

# django.contrib.auth
# ------------------------------------------------------------------------------
AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

# For Exposing browsable api urls. By default urls won't be exposed.
API_DEBUG = env.bool('API_DEBUG', default=False)

# rest_framework
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': '{{ cookiecutter.main_module }}.base.api.pagination.PageNumberPagination',
    'PAGE_SIZE': 30,

    # Default renderer classes for Rest framework
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],

    # 'Accept' header based versioning
    # http://www.django-rest-framework.org/api-guide/versioning/
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
    'DEFAULT_VERSION': '1.0',
    'ALLOWED_VERSIONS': ['1.0', ],
    'VERSION_PARAMETER': 'version',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10000/day',
    },
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',

        # Mainly used for api debug.
        'rest_framework.authentication.SessionAuthentication',
    ),
    "EXCEPTION_HANDLER": "{{ cookiecutter.main_module }}.base.exceptions.exception_handler",
}
# DJANGO_SITES
# ------------------------------------------------------------------------------
# see: http://django-sites.readthedocs.org
SITES = {
    "local": {"domain": "localhost:8000", "scheme": "http", "name": "localhost"},
}
SITE_ID = 'local'

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
# List of middleware classes to use.  Order is important; in the request phase,
# this middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES = (
    'log_request_id.middleware.RequestIDMiddleware',  # For generating/adding Request id for all the logs
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# DJANGO CORE
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
# Defaults to false, which is safe, enable them only in development.
DEBUG = env.bool('DJANGO_DEBUG', False)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = '{{ cookiecutter.timezone }}'

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# Languages we provide translations for
LANGUAGES = (
    ("en", _("English")),
)

# A tuple of directories where Django looks for translation files.
LOCALE_PATHS = (
    str(APPS_DIR.path("locale")),
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# The list of directories to search for fixtures
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# The Python dotted path to the WSGI application that Django's internal servers
# (runserver, runfcgi) will use. If `None`, the return value of
# 'django.core.wsgi.get_wsgi_application' is used, thus preserving the same
# behavior as previous versions of Django. Otherwise this should point to an
# actual WSGI application object.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'

# URL CONFIGURATION
# ------------------------------------------------------------------------------
ROOT_URLCONF = '{{ cookiecutter.main_module }}.urls'


# Use this to change base url path django admin
DJANGO_ADMIN_URL = env.str('DJANGO_ADMIN_URL', default='admin')

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.smtp.EmailBackend')

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db("DATABASE_URL", default="postgres://localhost/{{ cookiecutter.main_module }}"),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = 10
{% if cookiecutter.postgis == 'y' %}DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'{% endif %}

# TEMPLATE CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# STATIC FILE CONFIGURATION
# -----------------------------------------------------------------------------
# Absolute path to the directory static files should be collected to.
# Example: "/var/www/example.com/static/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR.path('.staticfiles'))

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://example.com/static/", "http://static.example.com/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# A list of locations of additional static files
STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
{%- if cookiecutter.add_sass_with_django_compressor.lower() == 'y' %}
    'compressor.finders.CompressorFinder',
{%- endif %}
)
{%- if cookiecutter.add_sass_with_django_compressor.lower() == 'y' %}

# Django Compressor Configuration
COMPRESS_CSS_FILTERS = [
    'django_compressor_autoprefixer.AutoprefixerFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_ENABLED = True
{%- endif %}

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR.path('.media'))

# URL that handles the media served from MEDIA_ROOT.
# Examples: "http://example.com/media/", "http://media.example.com/"
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

#  SECURITY
# -----------------------------------------------------------------------------
CSRF_COOKIE_HTTPONLY = False  # Allow javascripts to read CSRF token from cookies
SESSION_COOKIE_HTTPONLY = True  # Do not allow Session cookies to be read by javascript

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# django-log-request-id - Sending request id in response
REQUEST_ID_RESPONSE_HEADER = "REQUEST_ID"

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# Default logging for Django. This sends an email to the site admins on every
# HTTP 500 error. Depending on DEBUG, all other log records are either sent to
# the console (DEBUG=True) or discarded by mean of the NullHandler (DEBUG=False).
# See http://docs.djangoproject.com/en/dev/topics/logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'request_id': {
            '()': 'log_request_id.filters.RequestIDFilter'
        }
    },
    'formatters': {
        'complete': {
            # NOTE: make sure to include 'request_id' in filters when using this
            # formatter in any handlers.
            'format': '%(asctime)s:[%(levelname)s]:logger=%(name)s:request_id=%(request_id)s message="%(message)s"'
        },
        'simple': {
            'format': '%(levelname)s:%(asctime)s: %(message)s'
        },
        'null': {
            'format': '%(message)s',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'complete',
            'filters': ['request_id'],
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        '{{cookiecutter.main_module}}': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # Catch All Logger -- Captures any other logging
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
