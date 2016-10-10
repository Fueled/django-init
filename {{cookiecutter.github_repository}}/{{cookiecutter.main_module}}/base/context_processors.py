# -*- coding: utf-8 -*-

from django.conf import settings


def all_settings(context):
    return {'settings': settings}
