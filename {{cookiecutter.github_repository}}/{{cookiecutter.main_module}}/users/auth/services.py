# Stdlib Stuff
import uuid

# Third Party Stuff
from django.contrib.auth.tokens import default_token_generator
from rest_framework.exceptions import ValidationError
from django_sites import get_current
from mail_templated import send_mail
from django.conf import settings

# {{ cookiecutter.project_name }} Stuff
from .utils import encode_uid


def validate_uuid(uuid_value, raise_exception=False, error_message=None):
    """
    Validate whether the uuid_value is a valid uuid. If raise_exception is true,
    an exception would be raised if the value is not a valid uuid with the default error detail.

    :param uuid_value: uuid value to be validated
    :param raise_exception: whether to raise an exception if uuid is not valid
    :param error_message: Error detail message with which the error should be raised. Default detail is used otherwise
    :type uuid_value: string
    :type raise_exception: bool
    :type error_message: string
    :return: Boolean denoting whether the value is valid or not
    :rtype: bool
    """
    try:
        uuid.UUID(hex=str(uuid_value))
    except ValueError as exc:
        _error = error_message if error_message else exc.detail
    else:
        _error = {}

    if _error and raise_exception:
        raise ValidationError(_error)
    return not bool(_error)


def send_password_reset_mail(user):
    password_reset_path = settings.PASSWORD_RESET_CONFIRM_PATH.format(
        uid=encode_uid(user.pk),
        token=default_token_generator.make_token(user)
    )
    password_reset_url = "{frontend_app_base_url}/{password_reset_path}".format(
        frontend_app_base_url=settings.FRONTEND_APP_BASE_URL,
        password_reset_path=password_reset_path
    )
    ctx = {
        'site': get_current(),
        'user': user,
        'password_reset_url': password_reset_url,
    }
    to_emails = [user.email]
    from_email = settings.DEFAULT_FROM_EMAIL
    return send_mail(template_name='email/password_reset_mail.tpl',
                     context=ctx, from_email=from_email, recipient_list=to_emails)
