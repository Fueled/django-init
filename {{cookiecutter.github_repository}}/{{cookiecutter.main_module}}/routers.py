"""This urls.py is for all API related URLs.
"""

# Third Party Stuff
from rest_framework import routers

# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.users.auth.api import (
    AuthViewSet, CurrentUserViewSet
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'auth', AuthViewSet, base_name='auth')
router.register(r'me', CurrentUserViewSet, base_name='me')
