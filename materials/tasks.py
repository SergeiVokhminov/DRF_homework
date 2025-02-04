from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Subscription


@shared_task
def notification(course_objects_id, course_objects_title):
    """Отправка уведомление об обновлении курса по электронной почте."""

    courses = Subscription.objects.filter(course=course_objects_id)
    recipient_emails = [course.user.email for course in courses]
    send_mail(
        subject=f"Обновление курса {course_objects_title}",
        message=f"Привет!\nКурс {course_objects_title} был обновлён.\n",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_emails,
    )
