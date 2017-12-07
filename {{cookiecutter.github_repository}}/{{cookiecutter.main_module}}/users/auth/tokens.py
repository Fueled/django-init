# -*- coding: utf-8 -*-

# Third Party Stuff
import jwt
from django.apps import apps
from django.conf import settings

# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.base import exceptions as exc


def get_token_for_user(user, scope):
    """
    Generate a new signed token containing
    a specified user limited for a scope (identified as a string).
    """
    data = {
        "user_%s_id" % (scope): str(user.id),
    }
    return jwt.encode(data, settings.SECRET_KEY).decode()


def get_user_for_token(token, scope):
    """
    Given a selfcontained token and a scope try to parse and
    unsign it.

    If max_age is specified it checks token expiration.

    If token passes a validation, returns
    a user instance corresponding with user_id stored
    in the incoming token.
    """
    try:
        data = jwt.decode(token, settings.SECRET_KEY)
    except jwt.DecodeError:
        raise exc.NotAuthenticated("Invalid token")

    model_cls = apps.get_model("users", "User")

    try:
        user = model_cls.objects.get(pk=data["user_%s_id" % (scope)])
    except (model_cls.DoesNotExist, KeyError):
        raise exc.NotAuthenticated("Invalid token")
    else:
        return user
