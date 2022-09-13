# Third Party Stuff
from rest_framework import serializers

# {{ cookiecutter.main_module }} Stuff
from {{cookiecutter.main_module}}.users import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "first_name", "last_name", "email"]
