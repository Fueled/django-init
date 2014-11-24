# -*- coding: utf-8 -*-

# Standard Library
import json

# Third Party Stuff
from django.conf import settings
from django.http import HttpResponse
from django.views.defaults import server_error
from rest_framework import status


def api_server_error(request, *args, **kwargs):
    """
    JSON aware server 500 error response.

    Don't return html for a json type request.
    """
    if not settings.DEBUG and request.META.get('CONTENT_TYPE', None) == "application/json":
        return HttpResponse(json.dumps({"error": "Server application error"}),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return server_error(request, *args, **kwargs)
