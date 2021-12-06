# Third Party Stuff
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Hello World API",
        default_version="0.0.0",
        description="Add a short project description here.",
    ),
    public=True,
    permission_classes=[AllowAny],
)

swagger_schema_view = schema_view.with_ui('swagger', cache_timeout=0)
