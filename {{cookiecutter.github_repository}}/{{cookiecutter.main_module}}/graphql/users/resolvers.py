from django.contrib.auth import get_user_model


def resolve_users(info):
    return get_user_model().objects.all()
