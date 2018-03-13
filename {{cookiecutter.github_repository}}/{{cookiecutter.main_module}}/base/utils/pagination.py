# {{ cookiecutter.project_name }} Stuff
from {{ cookiecutter.main_module }}.base.api.pagination import PageNumberPagination


def paginated_response(request, queryset, serializer_class, extra_context=None):
    '''
    Returns `Response` object with pagination info after serializing the django
    `queryset` as per the `serializer_class` given and processing the current
    `page` from the `request` object.

    If `extra_context`(dict) is provided, it will be passed to the serializer_class
    as context variables.
    '''
    paginator = PageNumberPagination()
    paginated_queryset = paginator.paginate_queryset(queryset=queryset, request=request)
    serializer_context = {'request': request}

    if extra_context:
        serializer_context.update(extra_context)

    serializer = serializer_class(paginated_queryset, context=serializer_context, many=True)
    return paginator.get_paginated_response(data=serializer.data)
