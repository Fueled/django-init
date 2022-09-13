# -*- coding: utf-8 -*-
__version__ = "{{ cookiecutter.version }}"
{%- if cookiecutter.add_celery.lower() == 'y' %}

# {{ cookiecutter.main_module }} Stuff
from {{cookiecutter.main_module}}.celery import app as celery_app  # noqa
{%- endif %}
