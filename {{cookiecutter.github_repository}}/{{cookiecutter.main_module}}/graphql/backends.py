from django.contrib.auth import get_user_model
from {{cookiecutter.main_module}}.users.auth import tokens, backends

UserModel = get_user_model()


class GraphJWTAuthentication(backends.JWTAuthenticationMixin):
    def authenticate(self, request, **kwargs):
        auth_res = super().authenticate(request)
        try:
            user, _ = auth_res
        except TypeError:
            user = auth_res
        if user:
            return user
        return None

    def get_user(self, user_id):
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
