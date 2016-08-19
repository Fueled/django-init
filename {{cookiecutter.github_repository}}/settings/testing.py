from __future__ import absolute_import, unicode_literals

from .development import *  # noqa F405

MEDIA_ROOT = "/tmp"

SECRET_KEY = 'top-scret!'

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
INSTALLED_APPS += ("tests", )  # noqa: F405
{%- if cookiecutter.add_sass_with_django_compressor.lower() == 'y' %}

# Do this here, so that test are run without `postcss` as a requirement.
# Travis CI run with node 0.10.0 which is incompatible with the version
# postcss required.
# This causes the autoprefixer to not run on the complied css.
COMPRESS_CSS_FILTERS.remove('django_compressor_autoprefixer.AutoprefixerFilter')  # noqa: F405
{%- endif %}
