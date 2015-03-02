# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Third Party Stuff
from {{ cookiecutter.repo_name }}.base import response
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework import viewsets

from . import serializers
from .services import register_apple_device


class DeviceViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    @list_route(methods=["POST"])
    def add_ios_device(self, request):
        serializer = serializers.DeviceSerializer(data=request.DATA)
        if serializer.is_valid():
            device = register_apple_device(request.user, **serializer.data)
            return response.Ok({'token': device.token,
                                'user_id': device.user.id})
        else:
            return response.BadRequest(serializer.errors)
