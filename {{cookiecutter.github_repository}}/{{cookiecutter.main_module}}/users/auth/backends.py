"""
Authentication backends for rest framework.

This module exposes two backends: session and token.

The first (session) is a modified version of standard
session authentication backend of restframework with2
csrf token disabled.

And the second (token) implements own version of oauth2
like authentiacation but with selfcontained tokens. Thats
makes authentication totally stateles.

It uses django signing framework for create new
selfcontained tokens. This trust tokes from external
fraudulent modifications.
"""
# Third Party Stuff
from rest_framework.authentication import BaseAuthentication

from .tokens import get_user_for_token
from .utils import get_http_authorization


class JWTAuthenticationMixin:
    def authenticate(self, request):
        token = get_http_authorization(request)
        if not token:
            return None

        user = get_user_for_token(token, "authentication")

        return (user, token)

    def authenticate_header(self, request):
        return 'Bearer realm="api"'


class RestJWTAuthentication(JWTAuthenticationMixin, BaseAuthentication):
    """Self-contained stateles authentication implementation that work similar to OAuth2.

    It uses json web tokens (https://github.com/jpadilla/pyjwt) for trust
    data stored in the token.
    """
    pass
