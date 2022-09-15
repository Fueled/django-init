{%- if cookiecutter.add_graphql == "y" %}
import graphene
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required, superuser_required

from {{cookiecutter.main_module}}.users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class Query(object):
    me = graphene.Field(
        UserType,
        description='Return Current User\'s Information'
    )
    users = graphene.List(
        UserType,
        description='Return List of all Users'
    )

    @login_required
    def resolve_user(self, info, **kwargs):
        return info.context.user

    @superuser_required
    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()
{%- endif %}
