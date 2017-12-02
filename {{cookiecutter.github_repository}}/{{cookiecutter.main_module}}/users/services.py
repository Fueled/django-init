# Third Party Stuff
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate

# {{cookiecutter.main_module}} Stuff
from {{cookiecutter.main_module}}.base import exceptions as exc


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise exc.WrongArguments("Invalid username/password. Please try again!")

    return user


def create_user_account(email, password):
    user = get_user_model().objects.create_user(email=email, password=password)
    return user
