from django.contrib.auth import authenticate
from {{cookiecutter.main_module}}.users.auth.tokens import get_user_for_token
from {{cookiecutter.main_module}}.users.auth.utils import get_http_authorization


def _authenticate(request):
    is_anonymous = not hasattr(request, "user") or request.user.is_anonymous
    return is_anonymous and get_http_authorization(request) is not None


class JSONWebTokenMiddleware:
    def __init__(self):
        self.cached_allow_any = set()

    def resolve(self, next, root, info, **kwargs):
        context = info.context

        if _authenticate(context):

            token = get_http_authorization(context)
            user = get_user_for_token(token, "authentication")
            if user is not None:
                context.user = user

        return next(root, info, **kwargs)
