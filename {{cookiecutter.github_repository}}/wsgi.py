# -*- coding: utf-8 -*-
"""WSGI config for  project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.
"""

# Standard Library
import os

# Third Party Stuff
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
{%- if cookiecutter.add_sass_with_django_compressor.lower() == 'y' %}
from whitenoise.django import DjangoWhiteNoise


class DjangoCompressorWhiteNoise(DjangoWhiteNoise):
    """A sub-class of DjangoWhiteNoise to play nice with django compressor.

    DjangoWhiteNoise by-default doesn't add forever caching headers on the files
    generated with django-compressor as it doen't treat them as immutable. See
    original implementation of `is_immutable_file` for more details.
    """

    def is_immutable_file(self, path, url):
        """Determine whether given URL represents an immutable file.

        Adds a rule to the default implementation so that all the files in the
        COMPRESS_OUTPUT_DIR are recognized as immutable as well.
        """
        is_immutable = super(DjangoCompressorWhiteNoise, self).is_immutable_file(path, url)
        if not is_immutable:
            from django.conf import settings
            if settings.COMPRESS_OUTPUT_DIR in url:
                return True
        return is_immutable
{%- endif %}


# Read .env file and set key/value inside it as environement variables
# see: http://github.com/theskumar/python-dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ['DJANGO_SETTINGS_MODULE'] = '.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.production')

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
{%- if cookiecutter.add_sass_with_django_compressor.lower() == 'y' %}
application = DjangoCompressorWhiteNoise(get_wsgi_application())
{%- else %}
application = get_wsgi_application()
{%- endif %}

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
