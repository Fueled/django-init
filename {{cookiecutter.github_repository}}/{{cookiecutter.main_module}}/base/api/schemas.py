# Third Party Stuff
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
{%- if cookiecutter.add_graphql == "y" %}
import graphene
from graphene_django.debug import DjangoDebug
from {{ cookiecutter.main_module }}.users import schema as user_schema
{%- endif %}

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

{%- if cookiecutter.add_graphql == "y" %}
class Query(
    user_schema.Query,
    graphene.ObjectType
):
    debug = graphene.Field(DjangoDebug, name="_debug")


graphene_schema = graphene.Schema(query=Query)
{%- endif %}
