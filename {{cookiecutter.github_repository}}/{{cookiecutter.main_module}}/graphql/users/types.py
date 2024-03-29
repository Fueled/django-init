import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType

from {{cookiecutter.main_module}}.graphql.utils import CountableConnectionBase
from {{cookiecutter.main_module}}.users.auth import tokens
from {{cookiecutter.main_module}}.users.models import User


class CurrentUser(DjangoObjectType):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]
        interfaces = [relay.Node]


class AuthenticatedUser(DjangoObjectType):
    auth_token = graphene.String()

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]
        interfaces = [relay.Node]

    def resolve_auth_token(self, info):
        return tokens.get_token_for_user(self, "authentication")


class UserConnection(DjangoObjectType):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]
        filter_fields = {"id": ["exact"]}
        interfaces = (relay.Node,)
        connection_class = CountableConnectionBase
