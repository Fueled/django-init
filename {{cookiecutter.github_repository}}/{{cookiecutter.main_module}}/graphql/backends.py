from django.contrib.auth import get_user_model
from {{ cookiecutter.main_module }}.users.auth import tokens
from .utils import get_http_authorization

UserModel = get_user_model()


class JSONWebTokenBackend:
    def authenticate(self, request=None, **kwargs):
        if request is None or getattr(request, "_jwt_token_auth", False):
            return None

        token = get_http_authorization(request)

        if token is not None:
            return tokens.get_user_for_token(token, "authentication")

        return None

    def get_user(self, user_id):
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
