from graphene import relay
from graphene_django.types import DjangoObjectType

from {{cookiecutter.main_module}}.users.models import User


class CurrentUser(DjangoObjectType):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]


class UserConnection(DjangoObjectType):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]
        interfaces = (relay.Node,)
