from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from users.services import (
    create_stripe_product,
    create_stripe_price,
    create_stripe_session,
)


class UserCreateAPIView(generics.CreateAPIView):
    """Контроллер добавления пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListView(generics.ListAPIView):
    """Контроллер вывода списка пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """Контроллер детальной информации о пользователе."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    """Контроллер обновления пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(generics.DestroyAPIView):
    """Контроллер удаления пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentListView(generics.ListAPIView):
    """Контроллер оплаты."""

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ("date",)
    filterset_fields = (
        "course",
        "lesson",
        "payment_method",
    )


class PaymentCreateView(generics.CreateAPIView):
    """Контроллер создания оплаты."""

    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product = create_stripe_product(name=f"Оплата курса {payment.course.title}")
        price = create_stripe_price(payment.amount, product)
        session_id, payment_link_to_pay = create_stripe_session(price)
        payment.session_id = session_id
        payment.link_to_pay = payment_link_to_pay
        payment.save()
