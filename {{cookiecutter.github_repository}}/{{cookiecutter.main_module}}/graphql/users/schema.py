import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from {{cookiecutter.main_module}}.graphql.decorators import login_required, superuser_required
from {{cookiecutter.main_module}}.graphql.utils import filter_objects
from {{cookiecutter.main_module}}.users.models import User

from .types import UserConnection, CurrentUser
from .resolvers import get_all_users
from .mutations import SignUp, Login, PasswordChange, RequestPasswordReset, PasswordResetConfirm


class UserQueries(graphene.ObjectType):
    me = graphene.Field(
        CurrentUser, description="Return the currently authenticated user"
    )
    users = DjangoFilterConnectionField(
        UserConnection, description="Return list of all Users"
    )
    user_details = relay.Node.Field(UserConnection)

    @login_required
    def resolve_me(self, info):
        return info.context.user

    @superuser_required
    def resolve_users(self, info, **kwargs):
        qs = get_all_users(info)
        # add filters
        return qs

    @superuser_required
    def resolve_user_details(self, info, **kwargs):
        return filter_objects(
            User, kwargs['id']
        ).first()


class UserMutations(graphene.ObjectType):
    signup = SignUp.Field()
    login = Login.Field()
    password_change = PasswordChange.Field()
    password_reset = RequestPasswordReset.Field()
    password_reset_confirm = PasswordResetConfirm.Field()
