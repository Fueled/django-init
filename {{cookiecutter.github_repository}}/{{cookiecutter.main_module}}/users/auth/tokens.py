# Third Party Stuff
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.base import exceptions as exc

from .utils import decode_uuid_from_base64, encode_uuid_to_base64

HS256_ALGORITHM = "HS256"


def get_token_for_user(user, scope: str) -> str:
    """Generate a new signed token containing a specified user limited for a scope (identified as a string)."""
    data = {"user_%s_id" % (scope): str(user.id)}
    return jwt.encode(data, settings.SECRET_KEY, algorithm=HS256_ALGORITHM)


def get_user_for_token(token: str, scope: str):
    """
    Given a selfcontained token and a scope try to parse and
    unsign it.

    If max_age is specified it checks token expiration.

    If token passes a validation, returns
    a user instance corresponding with user_id stored
    in the incoming token.
    """
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[HS256_ALGORITHM])
    except jwt.DecodeError:
        raise exc.NotAuthenticated("Invalid token")

    model_cls = get_user_model()

    try:
        user = model_cls.objects.get(pk=data["user_%s_id" % (scope)])
    except (model_cls.DoesNotExist, KeyError):
        raise exc.NotAuthenticated("Invalid token")
    else:
        return user


def get_token_for_password_reset(user):
    return "{}::{}".format(
        encode_uuid_to_base64(user.pk), PasswordResetTokenGenerator().make_token(user)
    )


def get_user_for_password_reset_token(token):
    default_error_messages = {
        "invalid_token": "Invalid token or the token has expired",
        "user_not_found": "No user exists for given token",
    }
    try:
        uidb64, reset_token = token.split("::")
    except ValueError:
        raise exc.RequestValidationError(default_error_messages["invalid_token"])

    user_id = decode_uuid_from_base64(uidb64)
    if not user_id:
        raise exc.RequestValidationError(default_error_messages["invalid_token"])

    user = get_user_model().objects.filter(id=user_id).first()

    if not user:
        raise exc.RequestValidationError(default_error_messages["user_not_found"])

    if not PasswordResetTokenGenerator().check_token(user, reset_token):
        raise exc.RequestValidationError(default_error_messages["invalid_token"])

    return user
