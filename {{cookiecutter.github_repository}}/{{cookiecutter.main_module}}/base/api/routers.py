# Third Party Stuff
from rest_framework import routers


class SingletonRouter(routers.SimpleRouter):
    """Same as default router but without detail route and GET, POST, PUT, PATCH and
    DELETE maps to same url as list.

    See CurrentUserViewset for usages. This allows GenericViewSet to be used against
    a singleton resource. If `/me` endpoint represents currently logged in user
    you are able to `GET /me`, `PUT /me`, `DELETE /me` and can also add any list_routes like
    `POST /me/change-avatar`.
    """
    routes = [
        # Mapping for list, create, update, partial_update and delete function to http verb.
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
            detail=False,
            initkwargs={'suffix': ''}
        ),
        # Dynamically generated list routes.
        # Generated using @action decorator
        # on methods of the viewset.
        routers.DynamicRoute(
            url=r'^{prefix}/{url_path}$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        ),
    ]
