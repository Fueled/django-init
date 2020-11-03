# DRF helpers

## Permissions Per Action Helper

DRF allows us to set permissions on an entire viewset. 

```
class FooViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
```

`PermissionPerAction` mixin available in the `base` module allows us to set permission classes for each of the actions (`list`, `retrieve`, `create`, `partial_update`, `update` or any other custom actions) on the viewset.

```
import project_name.base.api.mixins import PermissionPerAction

class FooViewSet(PermissionPerAction, viewsets.ModelViewSet):
    permissions_per_action = {
        "create": [permissions.IsAuthenticated],
        "list": [permissions.AllowAny]
    }
```

## Multiple Serializers for a viewset

Similiar to permission classes, DRF allows us to only set one serializer per viewset. 

```
class FooViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FooSerializer
```

`MultipleSerializerMixin` available in the `base` module allows us to set different serializer classes for each of the actions (`list`, `retrieve`, `create`, `partial_update`, `update` or any other custom actions) on the viewset.

```
import project_name.base.api.mixins import MultipleSerializerMixin

class FooViewSet(MultipleSerializerMixin, viewsets.ModelViewSet):
    serializer_classes = {
        "create": serializers.CreateFooSerializer,
        "list": serializers.ReadFooSerializer
    }
```
