from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    """Поля для модели пользователя."""

    username = models.CharField(max_length=20, default="Пользователь")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone_number = models.CharField(
        max_length=35, verbose_name="Номер телефона", blank=True, null=True
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        help_text="Введите город",
        blank=True,
        null=True,
        default="город не указан"
    )
    avatar = models.ImageField(
        upload_to="photo/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите Ваш аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    """Поля для модели платежа."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Выберите пользователя",
        related_name="payments",
    )
    date = models.DateField(verbose_name="Дата оплаты", auto_now_add=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный курс",
        help_text="Выберите курс",
        blank=True,
        null=True,
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Отдельно оплаченный урок",
        help_text="Выберите урок",
        blank=True,
        null=True,
    )
    amount = models.PositiveIntegerField(
        verbose_name="Сумма оплаты", help_text="Введите сумму оплаты"
    )

    PAYMENT_METHODS = [
        ("cash", "Наличные"),
        ("transfer_to_account", "Перевод на счет"),
    ]
    payment_method = models.CharField(
        choices=PAYMENT_METHODS,
        max_length=50,
        verbose_name="Способ оплаты",
        help_text="Выберите способ оплаты",
        default="Наличные"
    )
    session_id = models.CharField(
        max_length=255,
        verbose_name="ID сессии",
        help_text="Введите ID сессии",
        blank=True,
        null=True,
        default="тестовый id"
    )
    link_to_pay = models.URLField(
        max_length=400,
        verbose_name="Ссылка на оплату",
        help_text="Добавьте ссылку на оплату",
        blank=True,
        null=True,
        default="https://testov.com"
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.user.email} за '{self.course.title if self.course else self.lesson.title}'"
