# Third Party Stuff
from django.core.exceptions import ImproperlyConfigured


class MultipleSerializerMixin(object):
    def get_serializer_class(self):
        """
        Look for serializer class in self.serializer_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class MyViewSet(MultipleSerializerMixin, ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }

            @list_route
            def my_action:
                ...

        If there's no serializer available for that action than
        the default serializer class will be returned as fallback.
        """
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()


class PermissionPerActionMixin:
    """
    Look for permission classes in self.permissions_per_action, which
    should be a dict mapping action name (key) to permission classes (value),
    i.e.:

        class MyViewSet(PermissionPerActionMixin, ViewSet):
            permission_classes = [permissions.IsAuthenticated]
            permissions_per_action = {
               'list': [DRFPermissions | CustomPermissions],
               'my_action': [DRFPermissions | CustomPermissions],
            }

            @list_route
            def my_action:
                ...

    If there are no permission classes available for that action than
    the default permission classes will be returned as fallback.
    """
    attr_name = "permissions_per_action"

    def get_permissions(self):
        action_permissions = getattr(self, self.attr_name)

        if not isinstance(action_permissions, dict):
            raise ImproperlyConfigured(f"{self.attr_name} should be a dict mapping.")

        if self.action in action_permissions.keys():
            self.permission_classes = action_permissions[self.action]

        return super().get_permissions()
