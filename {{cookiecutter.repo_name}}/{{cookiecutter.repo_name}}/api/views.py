# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
from functools import partial

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    '''List of api endpoints for this project.

    ### Authentication

    TODO

    ### Errors

    By default all error responses will include a key `details` in the body of
    the response.
    '''
    _reverse = partial(reverse, request=request, format=format)
    return Response({
        'api_root': _reverse('api_root'),
    })
