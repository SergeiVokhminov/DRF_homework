from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Пользователь"""
    class Meta:
        model = User
        fields = "__all__"
        # fields = ('email', 'password', 'phone', 'city', 'avatar')
