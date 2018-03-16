# Third Party Stuff
from django.contrib.auth import logout
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny, IsAuthenticated

# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.base import response
from {{cookiecutter.main_module}}.base.api.mixins import MultipleSerializerMixin
from {{cookiecutter.main_module}}.users import services as user_services

from . import serializers, services, tokens


class AuthViewSet(MultipleSerializerMixin, viewsets.GenericViewSet):

    permission_classes = [AllowAny, ]
    serializer_classes = {
        'login': serializers.LoginSerializer,
        'register': serializers.RegisterSerializer,
        'password_change': serializers.PasswordChangeSerializer,
        'password_reset': serializers.PasswordResetSerializer,
        'password_reset_confirm': serializers.PasswordResetConfirmSerializer,
    }

    @list_route(['POST', ])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_services.get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return response.Ok(data)

    @list_route(['POST', ])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_services.create_user_account(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return response.Created(data)

    @list_route(['POST', ])
    def logout(self, request):
        """
        Calls Django logout method; Does not work for UserTokenAuth.
        """
        logout(request)
        return response.Ok({"success": "Successfully logged out."})

    @list_route(['POST', ], permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return response.NoContent()

    @list_route(['POST', ])
    def password_reset(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_services.get_user_by_email(serializer.data['email'])
        if user:
            services.send_password_reset_mail(user)
        return response.Ok({'message': 'Further instructions will be sent to the email if it exists'})

    @list_route(['POST', ])
    def password_reset_confirm(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = tokens.get_user_for_password_reset_token(serializer.validated_data['token'])
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return response.NoContent()
