# -*- coding: utf-8 -*-
# Standard Library
import re
from uuid import UUID

# Third Party Stuff
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


def encode_uuid_to_base64(uuid_) -> str:
    """Returns a  urlsafe based64 encoded representation of a UUID object or UUID like string."""
    return urlsafe_base64_encode(force_bytes(uuid_))


def decode_uuid_from_base64(uuid_value: str):
    """Given a base64 encoded string, try to decode it to a valid UUID object.

    Returns a valid UUID value or None
    """
    try:
        return UUID(force_str(urlsafe_base64_decode(uuid_value)))
    except (ValueError, OverflowError, TypeError):
        return None


def get_http_authorization(request):
    auth_rx = re.compile(r"^Bearer (.+)$")
    if request is None or "HTTP_AUTHORIZATION" not in request.META:
        return None

    token_rx_match = auth_rx.search(request.META["HTTP_AUTHORIZATION"])
    if not token_rx_match:
        return None

    token = token_rx_match.group(1)
    return token
