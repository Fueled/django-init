# -*- coding: utf-8 -*-

# Standard Library
import threading

# Third Party Stuff
import factory
from django.conf import settings


class Factory(factory.DjangoModelFactory):
    class Meta:
        strategy = factory.CREATE_STRATEGY
        model = None
        abstract = True

    _SEQUENCE = 1
    _SEQUENCE_LOCK = threading.Lock()

    @classmethod
    def _setup_next_sequence(cls):
        with cls._SEQUENCE_LOCK:
            cls._SEQUENCE += 1
        return cls._SEQUENCE


class UserFactory(Factory):
    class Meta:
        model = settings.AUTH_USER_MODEL
        strategy = factory.CREATE_STRATEGY

    # modify this to USERNAME_FIELD for custom user model
    username = factory.Sequence(lambda n: "User{}".format(n))
    email = factory.Sequence(lambda n: 'user%04d@email.com' % n)
    password = factory.PostGeneration(lambda obj, *args, **kwargs: obj.set_password(obj.phone_number))


def create_user(**kwargs):
    "Create an user along with their dependencies"
    return UserFactory.create(**kwargs)
