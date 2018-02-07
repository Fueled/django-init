# Standard Library
from uuid import UUID

# Third Party Stuff
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


def encode_uuid_to_base64(uuid_) -> str:
    """Returns a  urlsafe based64 encoded representation of a UUID object or UUID like string.
    """
    return urlsafe_base64_encode(force_bytes(uuid_)).decode()


def decode_uuid_from_base64(uuid_value: str):
    """Given a base64 encoded string, try to decode it to a valid UUID object.

    Returns a valid UUID value or None
    """
    try:
        return UUID(force_text(urlsafe_base64_decode(uuid_value)))
    except (ValueError, OverflowError, TypeError):
        return None
