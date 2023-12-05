from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer

from career_toolbox.models import Specialization
from users.models import User


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class CustomUserSerializer(UserSerializer):
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
