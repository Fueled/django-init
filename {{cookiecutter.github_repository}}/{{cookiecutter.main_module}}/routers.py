# -*- coding: utf-8 -*-
"""This urls.py is for all API related URLs.
"""

# Third Party Stuff
from django.conf.urls import url
from rest_framework import routers

# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.users.auth.api import (
    AuthViewSet, CurrentUserView
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'auth', AuthViewSet, base_name='auth')

urlpatterns = router.urls + [
    url(r'^me$', CurrentUserView.as_view(), name='me')
]
