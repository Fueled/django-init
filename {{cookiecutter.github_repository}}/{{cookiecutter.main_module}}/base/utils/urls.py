# Third Party Stuff
import django_sites as sites
from django.conf import settings
from django.urls import reverse as django_reverse

URL_TEMPLATE = '{scheme}://{domain}/{path}'


def build_url(path, scheme='http', domain='localhost'):
    return URL_TEMPLATE.format(scheme=scheme, domain=domain, path=path.lstrip('/'))


def is_absolute_url(path):
    """Test wether or not `path` is absolute url.
    """
    return path.startswith('http')


def get_absolute_url(path, site_id=None):
    """Return a path as an absolute url.
    """
    if is_absolute_url(path):
        return path
    if site_id:
        site = sites.get_by_id(site_id)
    else:
        site = sites.get_current()
    return build_url(path, scheme=site.scheme, domain=site.domain)


def resolve_frontend_url(name, site_id='frontend', **kwargs):
    """Returns the absolute url for the frontend site.
    url
    resolve_front_urls('password-confirm', token="xyz", uuid="abc")
    """
    urls = settings.FRONTEND_URLS
    path = urls[name].format(**kwargs)
    return get_absolute_url(path=path, site_id=site_id)


def reverse(viewname, *args, **kwargs):
    """Same behavior as django's reverse but uses django_sites to compute absolute url.
    """
    return get_absolute_url(django_reverse(viewname, *args, **kwargs))
