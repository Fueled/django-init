# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def test_api_default_and_allowed_versions(settings):
    assert settings.REST_FRAMEWORK['DEFAULT_VERSION'] == '1.0'
    assert settings.REST_FRAMEWORK['ALLOWED_VERSIONS'] == ['1.0', ]
