# -*- coding: utf-8 -*-
import importlib


def import_from_string(val):
    """
    Attempt to import a class from a string representation.

    From: https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/settings.py
    """
    try:
        # Nod to tastypie's use of importlib.
        parts = val.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except ImportError as e:
        msg = "Could not import '%s' for setting. %s: %s." % (val, e.__class__.__name__, e)
        raise ImportError(msg)
