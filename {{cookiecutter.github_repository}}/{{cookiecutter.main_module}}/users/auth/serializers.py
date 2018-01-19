# Third Party Stuff
from django.contrib.auth import get_user_model, password_validation
from rest_framework import serializers

# {{ cookiecutter.project_name }} Stuff
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
        fields = ['email', ]

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


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    default_error_messages = {
        'invalid_password': 'Invalid password.'
    }

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError(self.error_messages['invalid_password'])
        return value

    def validate_new_password(self, value):
        # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#django.contrib.auth.password_validation.validate_password
        password_validation.validate_password(value)
        return value
