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

