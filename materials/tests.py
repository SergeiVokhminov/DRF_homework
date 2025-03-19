from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    """Тесты для уроков."""

    def setUp(self):
        """Метод для установки взаимодействия с данными."""
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(title="Test course", owner=self.user)
        self.lesson = Lesson.objects.create(
            title="Test lesson", owner=self.user, course=self.course
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_list(self):
        """Тест вывода списка уроков."""
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "title": self.lesson.title,
                    "picture": None,
                    "description": self.lesson.description,
                    "link_to_the_video": self.lesson.link_to_the_video,
                    "course": 1,
                    "owner": 1,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_lesson_create(self):
        """Тест создания уроков."""
        data = {
            "title": "New test",
            "link_to_the_video": "https://www.youtube.com/test/",
        }
        url = reverse("materials:lesson_create")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_detail(self):
        """Тест подробного вывода уроков."""
        url = reverse("materials:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(self.lesson.owner, self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_update(self):
        """Тест изменения уроков."""
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {"title": "New title test"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "New title test")

    def test_lesson_delete(self):
        """Тест удаления уроков."""
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):
    """Тест подписки на курс."""

    def setUp(self):
        """Метод для установки взаимодействия с данными."""
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(title="Test course", owner=self.user)
        self.new_course = Course.objects.create(title="New course", owner=self.user)
        self.subscription = Subscription.objects.create(
            user=self.user, course=self.course
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        """Тест создания подписки."""
        data = {"pk": self.new_course.id}
        url = reverse("materials:subscription")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Подписка была создана.")

    def test_subscription_delete(self):
        """Тест удаления подписки."""
        data = {"pk": self.course.id}
        url = reverse("materials:subscription")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Подписка была удалена.")
