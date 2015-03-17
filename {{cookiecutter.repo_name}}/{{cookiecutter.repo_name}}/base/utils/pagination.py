# -*- coding: utf-8 -*-

# {{ cookiecutter.project_name }} Stuff
from {{ cookiecutter.repo_name }}.base.api.pagination import PageNumberPagination


def paginated_response(request, queryset, serializer_class):
    '''
    Returns `Response` object with pagination info after serializing the django
    `queryset` as per the `serializer_class` given and processing the current
    `page` from the `request` object.
    '''
    paginator = PageNumberPagination()
    paginated_queryset = paginator.paginate_queryset(queryset=queryset, request=request)
    serializer_context = {'request': request}
    serializer = serializer_class(paginated_queryset, context=serializer_context, many=True)
    return paginator.get_paginated_response(data=serializer.data)
