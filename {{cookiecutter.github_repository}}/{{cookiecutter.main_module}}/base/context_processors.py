# -*- coding: utf-8 -*-

from django.conf import settings


def site_settings(context):
    return {'site_info': settings.SITE_INFO}
