# -*- coding: utf-8 -*-
'''
Pages App Routing.

Handles the top level site pages. You would probably like to add the pages like
homepage, about, terms and conditions, etc. in this app.
'''
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Top Level Pages
# ==============================================================================
urlpatterns = patterns('',
    url(r'^$',  # noqa
        TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'), name="about"),
    url(r'^robots\.txt$',
        TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots'),
    url(r'^humans\.txt$',
        TemplateView.as_view(template_name='humans.txt', content_type='text/plain'), name='humans'),
)
