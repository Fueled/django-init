# -*- coding: utf-8 -*-
'''Django settings for {{cookiecutter.project_name}} project.

see: https://docs.djangoproject.com/en/dev/ref/settings/
'''
from __future__ import print_function, unicode_literals

import os
from os.path import dirname, join

import dotenv
from configurations import Configuration, values


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
ROOT_DIR = dirname(dirname(__file__))
APP_DIR = join(ROOT_DIR, '{{ cookiecutter.repo_name }}')

# read and load variables in environement from .env file
# see: http://github.com/theskumar/python-dotenv
dotenv.load_dotenv(join(ROOT_DIR, ".env"))


# Common Configurations
# ========================================================================
class Common(Configuration):
    '''Common Configuration, overide them in it's sub-classes.'''

    # List of strings representing installed apps.
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django_sites',  # http://niwibe.github.io/django-sites/
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        # 'django.contrib.humanize',  # Useful template tags:

        '{{ cookiecutter.repo_name }}.base',
        '{{ cookiecutter.repo_name }}.pages',

        'django_extensions',  # http://django-extensions.readthedocs.org/
        'rest_framework',  # http://www.django-rest-framework.org/
        'versatileimagefield',  # https://github.com/WGBH/django-versatileimagefield/
    )

    # MIDDLEWARE CONFIGURATION
    # --------------------------------------------------------------------------
    # List of middleware classes to use.  Order is important; in the request phase,
    # this middleware classes will be applied in the order given, and in the
    # response phase the middleware will be applied in reverse order.
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    # CORE
    # --------------------------------------------------------------------------

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    # Defaults to false, which is safe, enable them only in development.
    DEBUG = values.BooleanValue(False)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG

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

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True

    # A secret key for this particular Django installation. Used in secret-key
    # hashing algorithms. Set this in your settings, or Django will complain
    # loudly.
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    SECRET_KEY = values.SecretValue(environ=True, environ_name='SECRET_KEY',
                                    environ_prefix='DJANGO')

    # The list of directories to search for fixtures
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
    FIXTURE_DIRS = (
        join(APP_DIR, 'fixtures'),
    )

    # The Python dotted path to the WSGI application that Django's internal servers
    # (runserver, runfcgi) will use. If `None`, the return value of
    # 'django.core.wsgi.get_wsgi_application' is used, thus preserving the same
    # behavior as previous versions of Django. Otherwise this should point to an
    # actual WSGI application object.
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = 'wsgi.application'

    # URL CONFIGURATION
    # --------------------------------------------------------------------------
    ROOT_URLCONF = '{{ cookiecutter.repo_name }}.urls'

    # MANAGER CONFIGURATION
    # --------------------------------------------------------------------------
    # People who get code error notifications.
    # In the format (('Full Name', 'email@example.com'), ('Full Name', 'anotheremail@example.com'))
    ADMINS = (
        ('{{ cookiecutter.project_name }} admin', '{{ cookiecutter.django_admin_email }}'),
    )

    # Not-necessarily-technical managers of the site. They get broken link
    # notifications and other various emails.
    MANAGERS = ADMINS

    # EMAIL CONFIGURATION
    # --------------------------------------------------------------------------
    EMAIL_BACKEND = values.Value('django.core.mail.backends.smtp.EmailBackend')

    # DATABASE CONFIGURATION
    # --------------------------------------------------------------------------
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(environ=True, environ_name='DATABASE_URL',
                                        environ_prefix='')

    # TEMPLATE CONFIGURATION
    # --------------------------------------------------------------------------
    # List of locations of the template source files, in search order.
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        join(APP_DIR, 'templates'),
    )

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # List of processors used by RequestContext to populate the context.
    # Each one should be a callable that takes the request object as its
    # only parameter and returns a dictionary to add to the context.
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
        # Your stuff: custom template context processers go here
    )

    # STATIC FILE CONFIGURATION
    # --------------------------------------------------------------------------
    # Absolute path to the directory static files should be collected to.
    # Example: "/var/www/example.com/static/"
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = join(ROOT_DIR, '.staticfiles')

    # URL that handles the static files served from STATIC_ROOT.
    # Example: "http://example.com/static/", "http://static.example.com/"
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # A list of locations of additional static files
    STATICFILES_DIRS = (
        # join(APP_DIR, 'static'),
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # MEDIA CONFIGURATION
    # --------------------------------------------------------------------------

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/var/www/example.com/media/"
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = join(ROOT_DIR, '.media')

    # URL that handles the media served from MEDIA_ROOT.
    # Examples: "http://example.com/media/", "http://media.example.com/"
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'

    # AUTHENTICATION CONFIGURATION
    # --------------------------------------------------------------------------
    AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

    # SLUGLIFIER
    AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
    # END SLUGLIFIER

    # LOGGING CONFIGURATION
    # --------------------------------------------------------------------------
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
            }
        },
        'formatters': {
            'complete': {
                'format': '%(levelname)s:%(asctime)s:%(module)s %(message)s'
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
                'class': 'django.utils.log.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
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
                'propagate': True,
                'level': 'INFO',
            },
            'django.request': {
                'handlers': ['mail_admins', 'console'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

    # Django Rest Framework
    # --------------------------------------------------------------------------
    REST_FRAMEWORK = {
        'PAGINATE_BY': 30,
        'PAGINATE_BY_PARAM': 'per_page',
        'MAX_PAGINATE_BY': 1000,
        # Use hyperlinked styles by default.
        # Only used if the `serializer_class` attribute is not set on a view.
        'DEFAULT_MODEL_SERIALIZER_CLASS': 'rest_framework.serializers.HyperlinkedModelSerializer',

        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',

            # Mainly used for api debug.
            'rest_framework.authentication.SessionAuthentication',
        ),
        "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
        "EXCEPTION_HANDLER": "{{ cookiecutter.repo_name }}.base.exceptions.exception_handler",
    }
{% if cookiecutter.celery == 'y' %}
    # CELERY CONFIGURATION
    # --------------------------------------------------------------------------
    from settings.celery import crontab  # noqa
    BROKER_URL = 'redis://localhost:6379/0'
    BROKER_TRANSPORT_OPTIONS = {'polling_interval': 0.3}
    CELERY_TIMEZONE = TIME_ZONE
    CELERY_TASK_SERIALIZER = 'pickle'
    CELERY_ACCEPT_CONTENT = ['pickle']
    # Periodic Tasks
    CELERYBEAT_SCHEDULE = {
    }
    # End Periodic Tasks
    # END CELERY CONFIGURATION
{% endif %}
    # DJANGO_SITES CONFIGURATION
    # --------------------------------------------------------------------------
    # see: http://django-sites.readthedocs.org
    SITES = {
        "local": {"domain": "localhost:8000", "scheme": "http", "name": "localhost"},
        "remote": {
            "domain": os.environ.get('SITE_DOMAIN'),
            "scheme": os.environ.get('SITE_SCHEME', 'https'),
            "name": os.environ.get('SITE_NAME'),
        },
    }

    SITE_ID = "remote"
