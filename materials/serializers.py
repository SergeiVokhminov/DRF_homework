from rest_framework import serializers

from materials.models import Course, Lesson, Subscription


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели урока."""

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели курса."""

    class Meta:
        model = Course
        fields = "__all__"


class CourseLessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели подсчета количества уроков."""

    lessons_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    subscription = serializers.SerializerMethodField(read_only=True)

    def get_lessons_count(self, obj):
        return obj.lessons.all().count()

    def get_subscription(self, course):
        user = self.context.get("request").user
        return Subscription.objects.filter(user=user, course=course).exists()

    class Meta:
        model = Course
        fields = ("title", "description", "lessons_count", "lessons")


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели подписки."""

    class Meta:
        model = Subscription
        fields = "__all__"
