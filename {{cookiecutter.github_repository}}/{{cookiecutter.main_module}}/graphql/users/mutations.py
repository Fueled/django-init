import graphene
from django.db import transaction
from graphene import relay
from graphql import GraphQLError

from .types import CurrentUser
from {{cookiecutter.main_module}}.users import services as user_services


class SignUp(relay.ClientIDMutation):

    class Input:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()

    @staticmethod
    def validate_email(email):
        if user_services.get_user_by_email(email):
            raise GraphQLError('User with email already exists')

    user = graphene.Field(CurrentUser)

    @classmethod
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, **data):
        cls.validate_email(data['email'])
        user = user_services.create_user_account(**data)
        return SignUp(user=user)
