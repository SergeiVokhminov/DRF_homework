from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("materials/", include("materials.urls"), name="materials"),
    path("users/", include("users.urls"), name="users"),
]
