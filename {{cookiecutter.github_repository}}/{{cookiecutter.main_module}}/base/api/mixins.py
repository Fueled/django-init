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
