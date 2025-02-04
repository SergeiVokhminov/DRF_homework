from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscription
from materials.pagination import PageSizePagination
from materials.serializers import (
    CourseLessonSerializer,
    CourseSerializer,
    LessonSerializer,
)
from users.permissions import IsModerators, IsOwner
from materials.tasks import notification


class CourseViewSet(viewsets.ModelViewSet):
    """Набор представлений для модели курс."""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = PageSizePagination

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseLessonSerializer
        return CourseSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (IsAuthenticated, ~IsModerators)
        elif self.action in ["update", "retrieve", "list"]:
            self.permission_classes = (IsAuthenticated, IsModerators | IsOwner)
        elif self.action == "destroy":
            self.permission_classes = (IsAuthenticated, IsOwner, ~IsModerators)
        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def perform_update(self, serializer):
        course_updated = serializer.save()
        course_updated_id = course_updated.id  # получаем id измененного курса
        course_updated_title = course_updated.title  # получаем название курса
        notification.delay(course_updated_id, course_updated_title)
        course_updated.save()


class LessonCreateView(generics.CreateAPIView):
    """Представление для создания модели урока."""

    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerators]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListView(generics.ListAPIView):
    """Представление для вывода списка уроков."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerators | IsOwner]
    pagination_class = PageSizePagination


class LessonDetailView(generics.RetrieveAPIView):
    """Представление для вывода деталей урока."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerators | IsOwner]


class LessonUpdateView(generics.UpdateAPIView):
    """Представление для обновления уроков."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerators | IsOwner]


class LessonDeleteView(generics.DestroyAPIView):
    """Представление для удаления урока."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerators | IsOwner]


class SubscriptionApiView(APIView):
    """Представление подписки на курс."""

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("pk")
        course_item = get_object_or_404(Course, pk=course_id)
        sub_item, created = Subscription.objects.get_or_create(
            user=user, course=course_item
        )
        if created:
            message = "Подписка была создана."
        else:
            sub_item.delete()
            message = "Подписка была удалена."
        return Response(message)
