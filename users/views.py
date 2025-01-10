from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Представления для пользовательской модели."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
