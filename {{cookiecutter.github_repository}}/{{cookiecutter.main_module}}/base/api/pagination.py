# Third Party Stuff
from rest_framework.pagination import PageNumberPagination as DrfPageNumberPagination


class PageNumberPagination(DrfPageNumberPagination):

    # Client can control the page using this query parameter.
    page_query_param = 'page'

    # Client can control the page size using this query parameter.
    # Default is 'None'. Set to eg 'page_size' to enable usage.
    page_size_query_param = 'per_page'

    # Set to an integer to limit the maximum page size the client may request.
    # Only relevant if 'page_size_query_param' has also been set.
    max_page_size = 1000


def paginated_response(request, queryset, serializer_class, extra_context=None):
    '''Utlity function to return a paginated response.

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
