from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_video_link


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели курса."""

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели урока."""

    # course = CourseSerializer(read_only=True)
    link_to_the_video = serializers.CharField(validators=[validate_video_link])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseLessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели подсчета количества уроков."""

    lessons_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    subscription = serializers.SerializerMethodField(read_only=True)

    def get_lessons_count(self, obj):
        """Метод получения количества уроков в курсе."""
        return obj.lessons.all().count()

    def get_subscription(self, course):
        """Метод проверки подписки на курс."""
        user = self.context.get("request").user
        return Subscription.objects.filter(user=user, course=course).exists()

    class Meta:
        model = Course
        fields = ("id", "title", "description", "lessons_count", "lessons", "subscription", "owner")


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели подписки."""

    class Meta:
        model = Subscription
        fields = "__all__"
