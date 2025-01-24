from django.db import models

from users.models import User


class Course(models.Model):
    """Поля для модели курса."""

    title = models.CharField(
        max_length=50, verbose_name="Название курса", help_text="Введите название курса"
    )
    picture = models.ImageField(
        upload_to="photo/picture/",
        verbose_name="Картинка",
        blank=True,
        null=True,
        help_text="Загрузите картинку",
    )
    description = models.TextField(
        max_length=250,
        verbose_name="Описание курса",
        blank=True,
        null=True,
        help_text="Введите описание курса",
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец",
                              help_text="Выберите владельца курса", related_name="courses", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Поля для модели урока."""

    title = models.CharField(
        max_length=50,
        verbose_name="Название",
        blank=True,
        null=True,
        help_text="Введите название урока",
    )
    picture = models.ImageField(
        upload_to="photo/picture/",
        verbose_name="Картинка",
        blank=True,
        null=True,
        help_text="Загрузите картинку",
    )
    description = models.TextField(
        max_length=250,
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание урока",
    )
    link_to_the_video = models.URLField(
        verbose_name="Ссылка на урок",
        help_text="Добавьте ссылку на урок",
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        related_name="lessons",
        verbose_name="Курс",
        help_text="Выберите курс",
        blank=True,
        null=True,
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец",
                              help_text="Выберите владельца урока", related_name="lessons", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
