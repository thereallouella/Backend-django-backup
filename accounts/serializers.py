from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import Files

User = get_user_model()


class CustomUserSerializer(UserCreateSerializer):
    is_active = serializers.BooleanField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['is_active'] = instance.is_active
        return representation

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'is_active')


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['id', 'file']
