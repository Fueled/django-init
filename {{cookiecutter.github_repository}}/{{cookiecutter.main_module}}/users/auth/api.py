# -*- coding: utf-8 -*-

# Third Party Stuff
from django.contrib.auth import logout
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework import generics, permissions

# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.base import response
from {{cookiecutter.main_module}}.users.models import User
from {{cookiecutter.main_module}}.base.api.mixins import MultipleSerializerMixin
from {{cookiecutter.main_module}}.users.services import create_user_account, get_and_authenticate_user

from . import serializers, backends


class AuthViewSet(MultipleSerializerMixin, viewsets.GenericViewSet):

    permission_classes = [AllowAny, ]
    serializer_classes = {
        'login': serializers.LoginSerializer,
        'register': serializers.RegisterSerializer,
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
    def logout(self, request):
        """
        Calls Django logout method and delete the Token object
        assigned to the current User object.
        """
        logout(request)
        return response.Ok({"success": "Successfully logged out."})


class CurrentUserView(generics.GenericAPIView):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    authentication_classes = (backends.UserTokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        return self.request.user

    def get(self, request):
        """
        Get logged in user profile
        """
        ctx = {'request': request}
        serializer = self.get_serializer(self.get_object(), context=ctx)
        return response.Ok(serializer.data)

    def put(self, request, *args, **kwargs):
        """
        Update logged in user profile
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        ctx = {'request': request}
        serializer = self.get_serializer(instance, data=request.data, context=ctx, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Ok(serializer.data)

    def patch(self, request, *args, **kwargs):
        """
        Update logged in user profile partially
        """
        kwargs['partial'] = True
        return self.put(request, *args, **kwargs)
