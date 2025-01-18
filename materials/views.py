from rest_framework import generics, viewsets

from materials.models import Course, Lesson
from materials.serializers import (CourseLessonSerializer, CourseSerializer,
                                   LessonSerializer)


class CourseViewSet(viewsets.ModelViewSet):
    """Набор представлений для модели курс."""

    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseLessonSerializer
        return CourseSerializer


class LessonCreateView(generics.CreateAPIView):
    """Представление для добавления модели урок."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListView(generics.ListAPIView):
    """Представление для вывода списка уроков."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDetailView(generics.RetrieveAPIView):
    """Представление для вывода деталей урока."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(generics.UpdateAPIView):
    """Представление для обновления уроков."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteView(generics.DestroyAPIView):
    """Представление для удаления уроков."""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
