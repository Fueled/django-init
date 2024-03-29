import graphene
from django.db import transaction
from django.contrib.auth import password_validation
from graphene import relay
from graphql import GraphQLError

from {{cookiecutter.main_module}}.users import services as user_services
from {{cookiecutter.main_module}}.users.auth import tokens
from {{cookiecutter.main_module}}.users.auth import services as auth_services
from .types import AuthenticatedUser, CurrentUser


class SignUp(relay.ClientIDMutation):
    class Input:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()

    @staticmethod
    def validate_email(email):
        if user_services.get_user_by_email(email):
            raise GraphQLError("User with email already exists")

    user = graphene.Field(CurrentUser)

    @classmethod
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, **data):
        cls.validate_email(data["email"])
        user = user_services.create_user_account(**data)
        return SignUp(user=user)


class Login(relay.ClientIDMutation):
    class Input:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    @staticmethod
    def validate_email(email):
        if not user_services.get_user_by_email(email):
            raise GraphQLError("User with email doesn't exist")

    user = graphene.Field(AuthenticatedUser)

    @classmethod
    def mutate_and_get_payload(cls, root, info, email, password):
        cls.validate_email(email)
        user = user_services.get_and_authenticate_user(email, password)
        return Login(user=user)


class PasswordChange(relay.ClientIDMutation):
    class Input:
        current_password = graphene.String(required=True)
        new_password = graphene.String(required=True)

    user = graphene.Field(AuthenticatedUser)

    @classmethod
    def mutate_and_get_payload(cls, root, info, current_password, new_password):
        user = info.context.user

        if not user.check_password(current_password):
            raise GraphQLError("invalid_password")

        password_validation.validate_password(new_password, user)

        user.set_password(new_password)
        user.save(update_fields=["password"])
        return PasswordChange(user=user)


class RequestPasswordReset(relay.ClientIDMutation):
    class Input:
        email = graphene.String(
            required=True,
            description="Email of the user that will be used for password recovery.",
        )

    message = graphene.String()

    @classmethod
    def clean_user(cls, email):
        user = user_services.get_user_by_email(email)
        if not user:
            raise GraphQLError("User with this email doesn't exist")
        if not user.is_active:
            raise GraphQLError("User with this email is inactive")
        return user

    @classmethod
    def mutate_and_get_payload(cls, root, info, email):
        user = cls.clean_user(email)

        auth_services.send_password_reset_mail(user)
        return RequestPasswordReset(
            message="Further instructions will be sent to the email if it exists"
        )


class PasswordResetConfirm(relay.ClientIDMutation):
    class Input:
        token = graphene.String(required=True)
        new_password = graphene.String(required=True)

    message = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, token, new_password):

        user = tokens.get_user_for_password_reset_token(token)
        password_validation.validate_password(new_password, user)

        user.set_password(new_password)
        user.save(update_fields=["password"])
        return PasswordResetConfirm(message="Password reset successfully.")
