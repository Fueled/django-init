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

# Standard Library
import re

# Third Party Stuff
from rest_framework.authentication import BaseAuthentication

from .tokens import get_user_for_token


class UserTokenAuthentication(BaseAuthentication):

    """
    Self-contained stateles authentication implementatrion
    that work similar to oauth2.
    It uses json web tokens (https://github.com/jpadilla/pyjwt) for trust
    data stored in the token.
    """

    auth_rx = re.compile(r"^Token (.+)$")

    def authenticate(self, request):
        if "HTTP_AUTHORIZATION" not in request.META:
            return None

        token_rx_match = self.auth_rx.search(
            request.META["HTTP_AUTHORIZATION"])
        if not token_rx_match:
            return None

        token = token_rx_match.group(1)
        user = get_user_for_token(token, "authentication")

        return (user, token)

    def authenticate_header(self, request):
        return 'Token realm="api"'
