import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType

from {{cookiecutter.main_module}}.users.models import User


class CountableConnectionBase(relay.Connection):
    """
        Extend connection class to display
        total count and edges count in paginated results
    """
    class Meta:
        abstract = True

    total_count = graphene.Int()
    edge_count = graphene.Int()

    @classmethod
    def resolve_total_count(cls, root, info, **kwargs):
        return root.length

    @classmethod
    def resolve_edge_count(cls, root, info, **kwargs):
        return len(root.edges)


class CurrentUser(DjangoObjectType):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]


class UserConnection(DjangoObjectType):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]
        filter_fields = {
            'id': ['exact']
        }
        interfaces = (relay.Node,)
        connection_class = CountableConnectionBase
