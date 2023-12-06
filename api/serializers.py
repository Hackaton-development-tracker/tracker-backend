from career_toolbox.models import Specialization
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from users.models import User


class SpecializationSerializer(serializers.ModelSerializer):
    """Сериализатор специальностей."""

    class Meta:
        model = Specialization
        fields = ('id', 'title')


class CustomUserSerializer(UserSerializer):
    """Cериализатор для получения юзера."""

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор регистрации юзеров."""
    email = serializers.EmailField(
        required=True, max_length=254)
    first_name = serializers.CharField(
        required=True, max_length=150)
    last_name = serializers.CharField(
        required=True, max_length=150)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')
