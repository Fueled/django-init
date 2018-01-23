# Third Party Stuff

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django_sites import get_current
from mail_templated import send_mail

# {{ cookiecutter.project_name }} Stuff
from .utils import encode_uid


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
