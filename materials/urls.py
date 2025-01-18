from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (
    CourseViewSet,
    LessonCreateView,
    LessonDeleteView,
    LessonDetailView,
    LessonListView,
    LessonUpdateView,
)

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="course")

# router = SimpleRouter()
# router.register(r"courses", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListView.as_view(), name="lesson_list"),
    path("lessons/create/", LessonCreateView.as_view(), name="lesson_create"),
    path("lessons/<int:pk>/", LessonDetailView.as_view(), name="lesson_detail"),
    path("lessons/update/<int:pk>/", LessonUpdateView.as_view(), name="lesson_update"),
    path("lessons/delete/<int:pk>/", LessonDeleteView.as_view(), name="lesson_delete"),
] + router.urls
