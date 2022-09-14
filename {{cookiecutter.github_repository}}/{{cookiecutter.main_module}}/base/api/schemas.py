# Third Party Stuff
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="{{ cookiecutter.project_name }} API",
        default_version="{{ cookiecutter.version }}",
        description="{{ cookiecutter.project_description }}",
    ),
    public=True,
    permission_classes=[AllowAny],
)

swagger_schema_view = schema_view.with_ui("swagger", cache_timeout=0)
