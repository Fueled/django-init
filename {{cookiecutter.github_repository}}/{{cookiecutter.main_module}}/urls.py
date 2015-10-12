# -*- coding: utf-8 -*-
'''Root url routering file.

You should put the url config in their respective app putting only a
refernce to them here.
'''
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .routers import router

handler500 = "{{ cookiecutter.main_module }}.base.views.server_error"

urlpatterns = [

    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        "{{ cookiecutter.main_module }}.base.views.root_txt_files", name='root-txt-files'),

    # Rest API
    url(r'^api/', include(router.urls)),

    # Browsable API
    url(r'^api/auth-n/', include('rest_framework.urls', namespace='rest_framework')),

    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

    # pages/ landing pages
    url(r'^', include("{{ cookiecutter.main_module }}.pages.urls", namespace="pages")),

    # Your stuff: custom urls go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', handler500),
    ]
