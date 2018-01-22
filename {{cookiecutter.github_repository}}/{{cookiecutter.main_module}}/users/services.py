# Third Party Stuff
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django_sites import get_current
from mail_templated import send_mail
# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.base import exceptions as exc


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise exc.WrongArguments("Invalid username/password. Please try again!")

    return user


def create_user_account(email, password, first_name="", last_name=""):
    user = get_user_model().objects.create_user(
        email=email, password=password, first_name=first_name, last_name=last_name
    )
    return user


def encode_uid(pk):
    return urlsafe_base64_encode(force_bytes(pk)).decode()


def decode_uid(pk):
    return force_text(urlsafe_base64_decode(pk))


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
