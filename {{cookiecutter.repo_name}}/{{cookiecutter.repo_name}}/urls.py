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
from django.contrib import admin


urlpatterns = patterns('',  # noqa
    url(r'^', include("{{ cookiecutter.repo_name }}.pages.urls", namespace="pages")),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    # url(r'^users/', include("users.urls", namespace="users")),

    # These URLS provide the login/logout functions for the browseable API.
    url(r'^api/auth-n/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('{{ cookiecutter.repo_name }}.routers.urls')),

    # Your stuff: custom urls go here

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^400/$', 'django.views.defaults.bad_request'),  # noqa
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    )
