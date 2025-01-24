from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.serializers import (CourseLessonSerializer, CourseSerializer,
                                   LessonSerializer)
from users.permissions import IsModerators, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """Набор представлений для модели курс."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

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


class LessonCreateView(generics.CreateAPIView):
    """Представление для добавления модели урок."""

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
    """Представление для удаления уроков."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerators | IsOwner]
