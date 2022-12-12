from django.contrib.auth import get_user_model


def get_all_users(info):
    return get_user_model().objects.all()
