# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Standard Library
import logging

# Third Party Stuff
from django.conf import settings
from integrations import INTEGRATION_MAP

from base.utils import import_from_string

from .models import Device

log = logging.getLogger(__name__)


def register_apple_device(user, token):
    try:
        device = Device.objects.get(token=token)
        device.user = user
        device.save()
    except Device.DoesNotExist:
        device = Device.objects.create(token=token, user=user)
    return device


def send_push_notification(*args, **kwargs):
    integration_class = import_from_string(settings.PUSH_NOTIFICATION_INTEGRATION)
    return integration_class().send_push_notification(*args, **kwargs)


def send_bulk_push_notification(*args, **kwargs):
    integration_class = import_from_string(settings.PUSH_NOTIFICATION_INTEGRATION)
    return integration_class().send_bulk_push_notification(*args, **kwargs)
