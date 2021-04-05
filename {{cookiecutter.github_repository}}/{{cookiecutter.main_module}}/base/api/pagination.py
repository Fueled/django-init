# Third Party Stuff
from rest_framework.pagination import (
    LimitOffsetPagination as DrfLimitOffsetPagination,
    CursorPagination as DrfCursorPagination,
)


class LimitOffsetPagination(DrfLimitOffsetPagination):

    # Client can control the offset using this query parameter.
    offset_query_param = 'offset'

    # Client can control the page size using this query parameter.
    # Default is 'None'. Set to eg 'page_size' to enable usage.
    limit_query_param = 'per_page'

    # Set to an integer to limit the maximum page size the client may request.
    # Only relevant if 'page_size_query_param' has also been set.
    max_limit = 1000


def limit_offset_paginated_response(request, queryset, serializer_class, extra_context=None):
    """Utlity function to return a paginated response.

    Returns `Response` object with pagination info after serializing the django
    `queryset` as per the `serializer_class` given and processing the current
    `page` from the `request` object.

    If `extra_context`(dict) is provided, it will be passed to the serializer_class
    as context variables.
    """
    paginator = LimitOffsetPagination()
    paginated_queryset = paginator.paginate_queryset(queryset=queryset, request=request)
    serializer_context = {"request": request}

    if extra_context:
        serializer_context.update(extra_context)

    serializer = serializer_class(
        paginated_queryset, context=serializer_context, many=True
    )
    return paginator.get_paginated_response(data=serializer.data)


class CursorPagination(DrfCursorPagination):
    """
    The cursor pagination implementation is necessarily complex.
    For an overview of the position/offset style we use, see this post:
    https://cra.mr/2011/03/08/building-cursors-for-the-disqus-api
    """

    # Ordering field used for cursor pagination
    # While using cursor pagination, ensure ordering field is part of that model
    ordering = '-created_at'

    # Client can control the cursor using this query parameter.
    cursor_query_param = 'cursor'

    # Client can control the page size using this query parameter.
    # Default is 'None'. Set to eg 'page_size' to enable usage.
    page_size_query_param = 'per_page'

    # Set to an integer to limit the maximum page size the client may request.
    # Only relevant if 'page_size_query_param' has also been set.
    max_page_size = None

    # The offset in the cursor is used in situations where we have a
    # nearly-unique index. (Eg millisecond precision creation timestamps)
    # We guard against malicious users attempting to cause expensive database
    # queries, by having a hard cap on the maximum possible size of the offset.
    offset_cutoff = 1000


def cursor_paginated_response(request, queryset, serializer_class, extra_context=None):
    """Utlity function to return a paginated response.

    Returns `Response` object with pagination info after serializing the django
    `queryset` as per the `serializer_class` given and processing the current
    `page` from the `request` object.

    If `extra_context`(dict) is provided, it will be passed to the serializer_class
    as context variables.
    """
    paginator = CursorPagination()
    paginated_queryset = paginator.paginate_queryset(queryset=queryset, request=request)
    serializer_context = {"request": request}

    if extra_context:
        serializer_context.update(extra_context)

    serializer = serializer_class(
        paginated_queryset, context=serializer_context, many=True
    )
    return paginator.get_paginated_response(data=serializer.data)
