"""This urls.py is for all API related URLs.
"""

# Third Party Stuff
from rest_framework import routers

# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.users.auth.api import (
    AuthViewSet, CurrentUserViewSet
)
from {{cookiecutter.main_module}}.base.utils.routers import BaseNameRouter

# Add all your router urls in urlpatters
urlpatterns = list()

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'auth', AuthViewSet, base_name='auth')

custom_router = BaseNameRouter()
custom_router.register(r'me', CurrentUserViewSet, base_name='me')

urlpatterns.extend(router.urls)
urlpatterns.extend(custom_router.urls)
