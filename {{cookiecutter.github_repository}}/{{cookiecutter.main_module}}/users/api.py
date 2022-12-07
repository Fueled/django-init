# Third Party Stuff
from rest_framework import viewsets

# {{ cookiecutter.main_module }} Stuff
from {{cookiecutter.main_module}}.base import response

from . import models, serializers


class CurrentUserViewSet(viewsets.GenericViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.filter(is_active=True)

    def get_object(self):
        return self.request.user

    def list(self, request):
        """Get logged in user profile"""
        serializer = self.get_serializer(self.get_object())
        return response.Ok(serializer.data)

    def partial_update(self, request):
        """Update logged in user profile"""
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Ok(serializer.data)
