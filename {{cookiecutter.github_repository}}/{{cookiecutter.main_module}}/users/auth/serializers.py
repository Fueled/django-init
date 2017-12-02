# -*- coding: utf-8 -*-

# Third Party Stuff
from django.contrib.auth import get_user_model
from rest_framework import serializers

# {{cookiecutter.main_module}} Stuff
from {{cookiecutter.main_module}}.users.models import User, UserManager

from .tokens import get_token_for_user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ['email', ]


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ['email', 'name']

    def validate_email(self, value):
        users = User.objects.filter(email__iexact=value)
        if users:
            raise serializers.ValidationError("Email is already taken.")
        return UserManager.normalize_email(value)


class AuthUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('id', 'name', 'auth_token', 'email')

    def get_name(self, obj):
        return obj.get_full_name()

    def get_auth_token(self, obj):
        return get_token_for_user(obj, "authentication")
