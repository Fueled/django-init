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
    try:
        uuid.UUID(hex=str(uuid_value))
    except ValueError as exc:
        _error = error_message if error_message else exc.detail
    else:
        _error = {}

    if raise_exception:
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
