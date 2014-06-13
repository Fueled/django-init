# -*- coding: utf-8 -*-
'''
Root url routering file.

You should put the url config in their respective app putting only a
refernce to them here.
'''
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include("pages.urls", namespace="pages")),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    # url(r'^users/', include("users.urls", namespace="users")),

    # REST API
    # url(r'^api/', include('api.urls')),

    # Your stuff: custom urls go here

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
