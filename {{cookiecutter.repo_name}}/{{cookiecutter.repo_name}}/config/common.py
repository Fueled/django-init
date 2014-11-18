# -*- coding: utf-8 -*-
'''Django settings for {{cookiecutter.project_name}} project.

see: https://docs.djangoproject.com/en/dev/ref/settings/
'''
from __future__ import print_function, unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join, dirname

from configurations import Configuration, values

BASE_DIR = dirname(dirname(__file__))

# read and load variables in environement from .env file
# see: http://github.com/theskumar/python-dotenv
import dotenv
dotenv.load_dotenv(join(BASE_DIR, ".env"))

import sys

if "test" in sys.argv:
    print("\033[1;91mNo django tests.\033[0m")
    print("Try: \033[1;33mpy.test\033[0m")
    sys.exit(0)


# Common Configurations
# ========================================================================
class Common(Configuration):

    '''Common Configuration, overide them in it's sub-classes.'''

    # APP CONFIGURATION
    # -----------------
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django_sites',  # http://niwibe.github.io/django-sites/
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Useful template tags:
        # 'django.contrib.humanize',

        # Admin
        'django.contrib.admin',
        'django_extensions',  # http://django-extensions.readthedocs.org/

        # Your stuff: custom apps go here
        'rest_framework',
        '{{ cookiecutter.repo_name }}.pages',
    )


    # MIDDLEWARE CONFIGURATION
    # Note: Order in which they are added are important
    MIDDLEWARE_CLASSES = (
        # Make sure djangosecure.middleware.SecurityMiddleware is the first
        # middleware class listed
        'djangosecure.middleware.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    # END MIDDLEWARE CONFIGURATION

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    # Defaults to false, which is safe, enable them only in development.
    DEBUG = values.BooleanValue(False)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG

    # SECRET CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    SECRET_KEY = values.SecretValue(environ=True, environ_name='SECRET_KEY',
                                    environ_prefix='DJANGO')
    # END SECRET CONFIGURATION

    # See:
    # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
    FIXTURE_DIRS = (
        join(BASE_DIR, 'fixtures'),
    )

    # MANAGER CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = (
        ('{{ cookiecutter.project_name }} admin',
         '{{ cookiecutter.django_admin_email }}'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
    MANAGERS = ADMINS
    # END MANAGER CONFIGURATION

    # EMAIL CONFIGURATION
    EMAIL_BACKEND = values.Value('django.core.mail.backends.smtp.EmailBackend')
    # END EMAIL CONFIGURATION

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # In a Windows environment this must be set to your system time zone.
    TIME_ZONE = '{{ cookiecutter.timezone }}'

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'en-us'

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True

    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = True

    # TEMPLATE CONFIGURATION
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

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        join(BASE_DIR, 'templates'),
    )

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'staticfiles')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See:
    # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        join(BASE_DIR, 'static'),
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    # END STATIC FILE CONFIGURATION

    # MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = join(BASE_DIR, 'media')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    # END MEDIA CONFIGURATION

    # URL Configuration
    ROOT_URLCONF = '{{ cookiecutter.repo_name }}.urls'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = 'wsgi.application'
    # End URL Configuration

    # AUTHENTICATION CONFIGURATION
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
    )

    # SLUGLIFIER
    AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
    # END SLUGLIFIER

    # LOGGING CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }
    # END LOGGING CONFIGURATION

    # DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(environ=True, environ_name='DATABASE_URL',
                                        environ_prefix='')
    # END DATABASE CONFIGURATION

    # Django Rest Framework
    REST_FRAMEWORK = {
        'PAGINATE_BY': 30,
        'PAGINATE_BY_PARAM': 'per_page',
        'MAX_PAGINATE_BY': 100,
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
            # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            # 'rest_framework.authentication.SessionAuthentication',
        ),
    }
    # End DRF

{% if cookiecutter.celery == 'y' %}
    # CELERY CONFIGURATION
    from celery import crontab  # noqa
    BROKER_URL = 'redis://localhost:6379/0'
    BROKER_TRANSPORT_OPTIONS = {'polling_interval': 0.3}
    CELERY_TIMEZONE = TIME_ZONE
    CELERY_TASK_SERIALIZER = 'pickle'
    CELERY_ACCEPT_CONTENT = ['pickle']
    # Periodic Tasks
    CELERYBEAT_SCHEDULE = {
    }
    # End Periodic Tasks
    # END CELERY CONFIGURATION {% endif %}

    # DJANGO_SITES
    # see: http://django-sites.readthedocs.org
    SITES = {
        "local": {"domain": "localhost:8000", "scheme": "http", "name": "localhost"},
        "remote": {
            "domain": values.Value(environ=True, environ_name='SITE_DOMAIN'),
            "scheme": values.Value("https", environ=True, environ_name='SITE_SCHEME'),
            "name": values.Value(environ=True, environ_name='SITE_NAME'),
        },
    }

    SITE_ID = "remote"
    # End django_sites
