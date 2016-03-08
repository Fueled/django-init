# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Standard Library
import sys

# Third Party Stuff
from django import http
from django.conf import settings
from django.shortcuts import render
from django.views.defaults import server_error as default_server_error


def server_error(request, *args, **kwargs):
    """
    JSON aware server 500 error response.

    Don't return html for a json type request.
    """
    exc_type, exc_obj, exc_tb = sys.exc_info()

    if not settings.DEBUG and request.META.get('CONTENT_TYPE', None) == "application/json":
        response_dict = {
          'error_type': exc_type.__name__ if exc_type else 'ServerError',
          'errors': [
            {
              'message': 'Server application error',
            }
          ]
        }
        return http.JsonResponse(data=response_dict, status=500)

    return default_server_error(request, *args, **kwargs)


def root_txt_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
