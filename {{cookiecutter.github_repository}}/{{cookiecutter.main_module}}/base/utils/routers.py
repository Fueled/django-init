# Third Party Stuff
from rest_framework import routers


class BaseNameRouter(routers.SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        routers.Route(
            url=r'^{prefix}$',
            mapping={'get': 'list', 'patch': 'partial_update', 'put': 'update'},
            name='{basename}',
            initkwargs={'suffix': 'List'}
        )
    ]
