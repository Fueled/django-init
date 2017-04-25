# -*- coding: utf-8 -*-
__version__ = '{{ cookiecutter.version }}'
__version_info__ = tuple([int(num) if num.isdigit() else num for num in __version__.replace('-', '.', 1).split('.')])
{%- if cookiecutter.add_celery.lower() == 'y' %}

from .celery import app as celery_app  # noqa
{%- endif %}
