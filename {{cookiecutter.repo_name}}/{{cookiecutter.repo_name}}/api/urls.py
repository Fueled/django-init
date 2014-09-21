'''This urls.py is for all API related URLs.

URL Naming Pattern (lowercased & underscored)
api_<app_name>_<model_name> or
api_<app_name>_<specific_action>
'''
from django.conf.urls import patterns, url

from api.views import api_root

urlpatterns = patterns('',
    url(r'^$', api_root, name='api_root'),  # noqa
)
