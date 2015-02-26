# -*- coding: utf-8 -*-

# Standard Library
import json
import sys

# Third Party Stuff
from django import http
from django.conf import settings
from django.views.defaults import server_error as dj_server_error


def server_error(request, *args, **kwargs):
    """
    JSON aware server 500 error response.

    Don't return html for a json type request.
    """
    exc_type, exc_obj, exc_tb = sys.exc_info()

    if not settings.DEBUG and request.META.get('CONTENT_TYPE', None) == "application/json":
        return http.HttpResponseServerError(json.dumps({
            "_error_message": "Server application error",
            "_error_type": "{0}.{1}".format(exc_type.__module__, exc_type.__name__)
            }), content_type="application/json")

    return dj_server_error(request, *args, **kwargs)
