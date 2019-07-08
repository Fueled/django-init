# -*- coding: utf-8 -*-
"""Root url routering file.

You should put the url config in their respective app putting only a
refernce to them here.
"""

# Third Party Stuff
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import include, path, re_path

from . import api_urls
from .base import views as base_views
from .base.api import schemas as api_schemas

admin.site.site_title = admin.site.site_header = '{{ cookiecutter.project_name }} Administration'
handler500 = base_views.server_error

# Top Level Pages
# ==============================================================================
urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    # Your stuff: custom urls go here
]

urlpatterns += [

    re_path(r'^(?P<filename>(robots.txt)|(humans.txt))$',
            base_views.root_txt_files, name='root-txt-files'),

    # Rest API
    path('api/', include(api_urls)),

    # Django Admin
    path('{}/'.format(settings.DJANGO_ADMIN_URL), admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.API_DEBUG:
    urlpatterns += [
        # Browsable API
        path('schema/', api_schemas.schema_view, name='schema'),
        path('api-playground/', api_schemas.swagger_schema_view, name='api-playground'),
        path('api/auth-n/', include('rest_framework.urls', namespace='rest_framework')),
    ]

if settings.DEBUG:
    from django.views import defaults as dj_default_views
    from django.urls import get_callable

    urlpatterns += [
        path('400/', dj_default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        path('403/', dj_default_views.permission_denied, kwargs={'exception': Exception('Permission Denied!')}),
        path('403_csrf/', get_callable(settings.CSRF_FAILURE_VIEW)),
        path('404/', dj_default_views.page_not_found, kwargs={'exception': Exception('Not Found!')}),
        path('500/', handler500),
    ]

    # Django Debug Toolbar
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
