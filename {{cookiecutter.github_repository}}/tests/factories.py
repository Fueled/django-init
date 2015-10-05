# -*- coding: utf-8 -*-

# Third Party Stuff
import factory
from django.conf import settings


class Factory(factory.DjangoModelFactory):
    class Meta:
        strategy = factory.CREATE_STRATEGY
        model = None
        abstract = True


class UserFactory(Factory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    # modify this to USERNAME_FIELD for custom user model
    username = factory.Sequence(lambda n: "User{}".format(n))
    email = factory.Sequence(lambda n: 'user%04d@email.com' % n)
    password = factory.PostGeneration(lambda obj, *args, **kwargs: obj.set_password(obj.phone_number))


def create_user(**kwargs):
    "Create an user along with their dependencies"
    return UserFactory.create(**kwargs)
