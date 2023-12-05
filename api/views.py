from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from djoser.views import UserViewSet

from career_toolbox.models import (Specialization,)
from users.models import User
from api.serializers import (SpecializationSerializer, CustomUserSerializer)


class SpecializationViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Category."""
    serializer_class = SpecializationSerializer
    queryset = Specialization.objects.all()

    @action(detail=True, methods=['post'])
    def add_spec(self, request, pk=None):
        specialization = self.get_object()
        user = request.user
        user.specializations.add(specialization)
        user.save()
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=200)


class CustomUserViewSet(UserViewSet):
    """Вьюсет для модели User и Subscribe"""
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
