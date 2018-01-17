# Standard Library
import sys

# Third Party Stuff
from django import http
from django.conf import settings
from django.shortcuts import render
from django.views.defaults import server_error as default_server_error


def server_error(request, *args, **kwargs):
    """JSON aware server 500 error response.

    As we don't want to return html response for a json request.
    """
    if not settings.DEBUG and request.META.get('CONTENT_TYPE', None) == 'application/json':
        exc_type, exc_obj, exc_tb = sys.exc_info()
        response_dict = {
            'error_type': exc_type.__name__ if exc_type else 'ServerError',
            'errors': [{'message': 'Server application error', }]
        }
        return http.JsonResponse(data=response_dict, status=500)

    return default_server_error(request, *args, **kwargs)


def csrf_failure(request, reason='', template_name='403_csrf.html'):
    """ Custom view used when request fails CSRF protection.

    Custom view is used because Django compressor complains if trying to
    use the in-built default view due to use `render` function. It keeps the
    logic but make things less magical.
    """
    from django.middleware.csrf import REASON_NO_REFERER, REASON_NO_CSRF_COOKIE
    ctx = {
        'reason': reason,
        'no_referer': reason == REASON_NO_REFERER,
        'no_cookie': reason == REASON_NO_CSRF_COOKIE,
        'DEBUG': settings.DEBUG,
    }
    return render(request, template_name=template_name, context=ctx, status=403)


def root_txt_files(request, filename):
    return render(request, filename, {}, content_type='text/plain')
