from rest_framework import serializers

from users.models import User, Payment


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Пользователь."""
    class Meta:
        model = User
        fields = "__all__"
        # fields = ('email', 'password', 'phone', 'city', 'avatar')


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели платежа."""
    class Meta:
        model = Payment
        fields = "__all__"
