"""Root url routering file.

You should put the url config in their respective app putting only a
refernce to them here.
"""

# Third Party Stuff
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from . import routers
from .base import views as base_views
from .base.api import schemas as api_schemas


handler500 = base_views.server_error

# Top Level Pages
# ==============================================================================
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    # Your stuff: custom urls go here
]

urlpatterns += [

    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        base_views.root_txt_files, name='root-txt-files'),

    # Rest API
    url(r'^api/', include(routers.router.urls)),

    # Django Admin
    url(r'^{}/'.format(settings.DJANGO_ADMIN_URL), admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.API_DEBUG:
    urlpatterns += [
        # Browsable API
        url('^schema/$', api_schemas.schema_view, name='schema'),
        url(r'^api-playground/$', api_schemas.swagger_schema_view, name='api-playground'),
        url(r'^api/auth-n/', include('rest_framework.urls', namespace='rest_framework')),
    ]

if settings.DEBUG:
    from django.views import defaults as dj_default_views
    from django.urls import get_callable

    urlpatterns += [
        url(r'^400/$', dj_default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', dj_default_views.permission_denied, kwargs={'exception': Exception('Permission Denied!')}),
        url(r'^403_csrf/$', get_callable(settings.CSRF_FAILURE_VIEW)),
        url(r'^404/$', dj_default_views.page_not_found, kwargs={'exception': Exception('Not Found!')}),
        url(r'^500/$', handler500),
    ]

    # Django Debug Toolbar
    try:
        import debug_toolbar
        urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)), ]
    except ImportError:
        pass

    # Livereloading
    try:
        from devrecargar.urls import urlpatterns as devrecargar_urls
        urlpatterns += [url(r'^devrecargar/', include((devrecargar_urls, 'devrecargar', ), namespace='devrecargar'))]
    except ImportError:
        pass
