from datetime import timedelta
from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def user_last_login():
    """Проверка время последнего входа."""

    today = timezone.now().date()
    users = User.objects.all()
    for user in users:
        if not user.last_login:
            user.is_active = False
            user.save()
        elif today - user.last_login.date() > timedelta(days=30):
            user.is_active = False
            user.save()
