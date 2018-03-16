"""This urls.py is for all API related URLs.
"""

# Third Party Stuff
from rest_framework.routers import DefaultRouter

# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.base.utils.routers import SingletonRouter
from {{cookiecutter.main_module}}.users.auth.api import (
    AuthViewSet, CurrentUserViewSet
)

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter()

# register all the viewset below.
default_router.register('auth', AuthViewSet, base_name='auth')
singleton_router.register('me', CurrentUserViewSet, base_name='me')

# combine the urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = default_router.urls + singleton_router.urls
