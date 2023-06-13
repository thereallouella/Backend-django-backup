from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import Listing

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


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'location', 'description', 'price', 'distant', 'tenant', 'essentials', 'contact_number',
                  'picture']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
