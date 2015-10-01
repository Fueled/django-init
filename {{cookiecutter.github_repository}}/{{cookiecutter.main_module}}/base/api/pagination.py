# -*- coding: utf-8 -*-
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
