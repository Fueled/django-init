# -*- coding: utf-8 -*-
__version__ = "{{ cookiecutter.version }}"
{%- if cookiecutter.add_celery.lower() == 'y' %}

from .celery import app as celery_app  # noqa
{%- endif %}
