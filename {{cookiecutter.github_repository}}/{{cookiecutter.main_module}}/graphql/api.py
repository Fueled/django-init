# Third Party Stuff
import graphene
from graphene_django.debug import DjangoDebug

from .users.schema import UserMutations, UserQueries


class Query(UserQueries):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(UserMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
