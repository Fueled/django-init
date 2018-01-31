# Third Party Stuff
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers

# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.users.services import get_user_by_email
from {{cookiecutter.main_module}}.users.models import UserManager
from .tokens import get_token_for_user
from .utils import decode_uid


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, value):
        user = get_user_by_email(email=value)
        if user:
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
        'invalid_password': 'Current password does not match'
    }

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError(self.default_error_messages['invalid_password'])
        return value

    def validate_new_password(self, value):
        # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#django.contrib.auth.password_validation.validate_password
        password_validation.validate_password(value)
        return value


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    uid = serializers.CharField(required=True)
    token = serializers.CharField(required=True)

    default_error_messages = {
        'invalid_uid': 'Invalid or malformed uid',
        'invalid_token': 'Invalid token or the token has expired'
    }

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value

    def validate_uid(self, value):
        """
        Validate the encoded user id and add a user attribute to the serializer.
        The user attribute is used in the validate_token method and the api view.
        """
        try:
            user_id = decode_uid(value)
            self.user = get_user_model().objects.get(id=user_id)
        except (get_user_model().DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError(self.default_error_messages['invalid_uid'])
        return value

    def validate_token(self, value):
        if not default_token_generator.check_token(self.user, value):
            raise serializers.ValidationError(self.default_error_messages['invalid_token'])
        return value
