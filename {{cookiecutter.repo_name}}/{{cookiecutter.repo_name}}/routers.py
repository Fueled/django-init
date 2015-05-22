# -*- coding: utf-8 -*-
'''This urls.py is for all API related URLs.

URL Naming Pattern (lowercased & underscored)
<app_name>_<model_name> or
<app_name>_<specific_action>

For base name use:
<app_name>
'''
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
