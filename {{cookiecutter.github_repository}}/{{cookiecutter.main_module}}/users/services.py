# Third Party Stuff
from django.contrib.auth import get_user_model, authenticate
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django_sites import get_current

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


def send_mail(to_email, from_email, subject, text_body, html_body, context=None):

    subject = render_to_string(subject, context)
    text_body = render_to_string(text_body, context)
    html_body = render_to_string(html_body, context)

    # sanitize subject to not contain any new lines
    subject = ''.join(subject.splitlines())
    msg = EmailMultiAlternatives(subject=subject, body=text_body,
                                 from_email=from_email, to=[to_email])
    msg.attach_alternative(content=html_body, mimetype="text/html")
    return msg.send()


def send_password_reset_mail(user):
    ctx = {
        'site': get_current(),
        'user': user,
        'url': settings.PASSWORD_RESET_CONFIRM_URL.format(
            uid=encode_uid(user.id),
            token=default_token_generator.make_token(user)
        ),
        'frontend_domain': settings.FRONTEND_DOMAIN,
    }
    to_email = [user.email]
    from_email = settings.FROM_EMAIL
    return send_mail(from_email=from_email,
                     to_email=to_email,
                     subject='email/password_reset_mail_subject.txt',
                     text_body='email/password_reset_mail_body.txt',
                     html_body='email/password_reset_mail_body.html',
                     context=ctx)
