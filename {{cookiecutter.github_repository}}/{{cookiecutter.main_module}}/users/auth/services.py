# Third Party Stuff

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django_sites import get_current
from mail_templated import send_mail

# {{ cookiecutter.project_name }} Stuff
from .utils import encode_uid


def send_password_reset_mail(user):
    ctx = {
        'site': get_current(),
        'user': user,
        'url': settings.PASSWORD_RESET_CONFIRM_URL.format(
            uid=encode_uid(user.pk),
            token=default_token_generator.make_token(user)
        ),
        'frontend_domain': settings.FRONTEND_DOMAIN,
    }
    to_emails = [user.email]
    from_email = settings.FROM_EMAIL
    return send_mail('email/password_reset_mail.tpl', ctx, from_email, to_emails)
