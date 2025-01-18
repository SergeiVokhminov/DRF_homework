from django.urls import path

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, PaymentListView, UserUpdateApiView, UserRetrieveApiView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"user", UserViewSet, basename="user")

urlpatterns = [
    path("user/update/<int:pk>/", UserUpdateApiView.as_view(), name="user_update"),
    path("user/retrieve/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"),
    path("payments/", PaymentListView.as_view(), name="payments_list"),
] + router.urls
