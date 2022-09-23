# Third Party Stuff
import graphene
import graphql_jwt
from graphene_django.debug import DjangoDebug

from .users.schema import UserQueries
from .users.mutations import UserMutations


class Query(
    UserQueries
):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(
    UserMutations
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
