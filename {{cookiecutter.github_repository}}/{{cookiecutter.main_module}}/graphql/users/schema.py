import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required, superuser_required

from .types import UserConnection, CurrentUser
from .resolvers import get_all_users


class UserQueries(graphene.ObjectType):
    me = graphene.Field(
        CurrentUser, description="Return the currently authenticated user"
    )
    users = DjangoFilterConnectionField(
        UserConnection, description="Return list of all Users"
    )

    @login_required
    def resolve_me(self, info):
        return info.context.user

    @superuser_required
    def resolve_users(self, info, **kwargs):
        qs = get_all_users(info)
        # add filters
        return qs


class UserMutations(graphene.ObjectType):
    signup = SignUp.Field()
