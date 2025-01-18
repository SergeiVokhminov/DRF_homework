from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import (PaymentListView, UserRetrieveApiView,
                         UserUpdateApiView, UserViewSet)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"user", UserViewSet, basename="user")

urlpatterns = [
    path("user/update/<int:pk>/", UserUpdateApiView.as_view(), name="user_update"),
    path(
        "user/retrieve/<int:pk>/", UserRetrieveApiView.as_view(), name="user_retrieve"
    ),
    path("payments/", PaymentListView.as_view(), name="payments_list"),
] + router.urls
