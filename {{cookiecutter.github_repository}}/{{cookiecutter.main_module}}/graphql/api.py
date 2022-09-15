# Third Party Stuff
{%- if cookiecutter.add_graphql == "y" %}
import graphene
from graphene_django.debug import DjangoDebug

from . import schema as user_schema


class Query(
    user_schema.Query,
    graphene.ObjectType
):
    debug = graphene.Field(DjangoDebug, name="_debug")


graphene_schema = graphene.Schema(query=Query)
{%- endif %}
