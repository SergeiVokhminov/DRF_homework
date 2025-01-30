from django.contrib import admin

from .models import Course, Lesson, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    search_fields = ("title", "description")
    list_filter = ("title", "description")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "course")
    search_fields = ("title", "description", "course")
    list_filter = ("title", "description", "course")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course")
    search_fields = ("user", "course")
    list_filter = ("user", "course")
