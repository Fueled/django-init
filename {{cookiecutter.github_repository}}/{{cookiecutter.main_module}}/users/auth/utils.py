# -*- coding: utf-8 -*-
# Standard Library
from uuid import UUID

# Third Party Stuff
{%- if cookiecutter.add_graphene == "y" %}
from django.contrib.auth import get_user_model
{%- endif %}

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


{%- if cookiecutter.add_graphene == "y" %}
def get_user_by_id(user_id):
    user_model = get_user_model()
    try:
        return user_model.objects.get(id=user_id)
    except user_model.DoesNotExist:
        return None
{%- endif %}
