# Third Party Stuff
from rest_framework import routers


class SingletonRouter(routers.SimpleRouter):
    """Same as default router but without detail route and GET, POST, PUT, PATCH and
    DELETE maps to same url as list.
    """
    routes = [
        # List route.
        routers.Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
                'post': 'create',
                'patch': 'partial_update',
                'put': 'update',
                'delete': 'destroy',
            },
            name='{basename}',
            initkwargs={'suffix': ''}
        ),
        # Dynamically generated list routes.
        # Generated using @list_route decorator
        # on methods of the viewset.
        routers.DynamicListRoute(
            url=r'^{prefix}/{methodname}{trailing_slash}$',
            name='{basename}-{methodnamehyphen}',
            initkwargs={}
        ),
    ]
