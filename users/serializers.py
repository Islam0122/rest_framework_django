from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    confirmation_code = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirmation_code']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, is_active=False)
        confirmation_code = models.ConfirmationCode.objects.create(user=user)
        confirmation_code.generate_code()
        confirmation_code.save()
        user.confirmation_code = confirmation_code.code  # assign the code to the user
        return user
