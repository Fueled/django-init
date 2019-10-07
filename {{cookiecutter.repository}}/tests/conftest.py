"""
This module is used to provide configuration, fixtures, and plugins for pytest.
It may be also used for extending doctest's context:
1. https://docs.python.org/3/library/doctest.html
2. https://docs.pytest.org/en/latest/doctest.html
"""

# Standard Library
import functools
from unittest import mock

# Third Party Stuff
import pytest


class PartialMethodCaller:
    def __init__(self, obj, **partial_params):
        self.obj = obj
        self.partial_params = partial_params

    def __getattr__(self, name):
        return functools.partial(getattr(self.obj, name), **self.partial_params)


@pytest.fixture(autouse=True, scope="function")
def cleared_cache():
    """Fixture that exposes django cache, which is empty to start with.

    This fixture also makes sures that cache is cleared before running each and every test case.
    """
    from django.core.cache import cache

    cache.clear()
    return cache


@pytest.fixture(autouse=True, scope="function")
def media_root(settings, tmpdir_factory):
    """Forces django to save media files into temp folder."""
    settings.MEDIA_ROOT = tmpdir_factory.mktemp("media", numbered=True)
    return settings.MEDIA_ROOT


@pytest.fixture
def client():
    """Django Test Client, with some convenient overriden methods.
    """
    from django.test import Client

    class _Client(Client):
        def login(
            self,
            user=None,
            backend="django.contrib.auth.backends.ModelBackend",
            **credentials
        ):
            """Modified login method, which allows setup an authenticated session with just passing in the
            user object, if provided.
            """
            if user is None:
                return super().login(**credentials)

            with mock.patch("django.contrib.auth.authenticate") as authenticate:
                user.backend = backend
                authenticate.return_value = user
                return super().login(**credentials)

        @property
        def json(self):
            """Add json method on the client for sending json type request.

            Usages:
            >>> import json
            >>> url = reverse("api-login")
            >>> client.json.get(url)
            >>> client.json.post(url, data=json.dumps(payload))
            """
            return PartialMethodCaller(
                obj=self, content_type='application/json;charset="utf-8"'
            )

    return _Client()
