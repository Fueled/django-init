# Third Party Stuff
from django import template

from ..utils.urls import resolve_frontend_url as _resolve_frontend_url

register = template.Library()


@register.simple_tag
def resolve_frontend_url(name, **kwargs):
    """Templatetag to render absolute urls for frontend app via it's name.

    It makes use of the mapping in FRONTEND_URLS in settings, combined with
    FRONTEND_SITE_SCHEME and FRONTEND_SITE_DOMAIN and configuration.

    Usages:
    ```
    {% load resolve_frontend_url from urls_extra %}

    {% resolve_frontend_url "home" %}
    {% resolve_frontend_url "password-reset" token=token %}
    ```
    """
    return _resolve_frontend_url(name, **kwargs)
