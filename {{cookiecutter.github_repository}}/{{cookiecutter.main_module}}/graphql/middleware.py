from django.contrib.auth import authenticate
from django.contrib.auth.middleware import get_user
from django.contrib.auth.models import AnonymousUser
from .utils import get_http_authorization


def _authenticate(request):
    is_anonymous = not hasattr(request, "user") or request.user.is_anonymous
    return is_anonymous  and get_http_authorization(request) is not None


class JSONWebTokenMiddleware:
    def __init__(self):
        self.cached_allow_any = set()

    def resolve(self, next, root, info, **kwargs):
        context = info.context

        if _authenticate(context):

            user = authenticate(request=context, **kwargs)

            if user is not None:
                context.user = user

        return next(root, info, **kwargs)
