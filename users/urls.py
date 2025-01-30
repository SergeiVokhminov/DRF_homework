from django.urls import path
from rest_framework.permissions import AllowAny

# from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    PaymentListView,
    UserCreateAPIView,
    UserDeleteView,
    UserDetailView,
    UserListView,
    UserUpdateView,
)

app_name = UsersConfig.name

# router = DefaultRouter()
# router.register(r"user", UserViewSet, basename="user")

urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("", UserListView.as_view(), name="user_list"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("user/update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("user/delete/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
    path("payments/", PaymentListView.as_view(), name="payments_list"),
]  # + router.urls
