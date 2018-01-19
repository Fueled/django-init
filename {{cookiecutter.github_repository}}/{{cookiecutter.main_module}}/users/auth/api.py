# Third Party Stuff
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny

# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.base import response
from {{cookiecutter.main_module}}.base.api.mixins import MultipleSerializerMixin
from {{cookiecutter.main_module}}.users.services import create_user_account, get_and_authenticate_user

from . import serializers


class AuthViewSet(MultipleSerializerMixin, viewsets.GenericViewSet):

    permission_classes = [AllowAny, ]
    serializer_classes = {
        'login': serializers.LoginSerializer,
        'register': serializers.RegisterSerializer,
        'password_change': serializers.PasswordChangeSerializer,
    }

    @list_route(['POST', ])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return response.Ok(data)

    @list_route(['POST', ])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return response.Created(data)

    @list_route(['POST', ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return response.NoContent()
