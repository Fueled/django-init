# Third Party Stuff
from django.conf import settings
from mail_templated import send_mail

# {{ cookiecutter.project_name }} Stuff
from .tokens import get_token_for_password_reset


def send_password_reset_mail(user, template_name='email/password_reset_mail.tpl'):
    ctx = {
        'user': user,
        'token': get_token_for_password_reset(user),
    }
    return send_mail(from_email=settings.DEFAULT_FROM_EMAIL,
                     recipient_list=[user.email],
                     template_name=template_name,
                     context=ctx)
