# Third Party Stuff
import graphene
from graphene_django.debug import DjangoDebug

from .user_schema import UserQueries


class Query(
    UserQueries
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query)
