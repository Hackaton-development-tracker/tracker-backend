from career_toolbox.models import Specialization
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import CustomUserSerializer, SpecializationSerializer
from users.models import User


class CustomUserViewSet(UserViewSet):
    """Вьюсет для модели User."""
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer


class SpecializationViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Specialization."""
    serializer_class = SpecializationSerializer
    queryset = Specialization.objects.all()

    @action(detail=True, methods=['post'])
    def add_spec(self, request, pk=None):
        """Выбор специальности."""
        specialization = self.get_object()
        user = request.user
        user.specializations.add(specialization)
        user.save()
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
