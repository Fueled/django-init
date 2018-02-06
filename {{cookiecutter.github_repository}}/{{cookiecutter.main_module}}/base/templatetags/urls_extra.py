from django import template

from ..utils.urls import resolve_frontend_url as _resolve_frontend_url

register = template.Library()


@register.simple_tag
def resolve_frontend_url(name, **kwargs):
    return _resolve_frontend_url(name, **kwargs)
