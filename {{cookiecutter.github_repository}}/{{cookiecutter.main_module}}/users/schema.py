{%- if cookiecutter.add_graphene == "y" %}
from .models import User
import graphene
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required, superuser_required


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class Query(object):
    user = graphene.Field(
        UserType,
        description='Return Current User\'s Information'
    )
    all_users = graphene.List(
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
