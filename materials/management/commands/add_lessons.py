from django.core.management import call_command
from django.core.management.base import BaseCommand

from materials.models import Lesson


class Command(BaseCommand):
    """Очистка базы данных уроков и загрузка сохраненных ранее данных из фикстур в базу данных."""

    help = "Заполнить базу данных уроков из фикстур."

    def handle(self, *args, **kwargs):
        """Функция очистки базы данных и заполнения."""
        Lesson.objects.all().delete()

        call_command("loaddata", "fixture/lessons_fixture.json")
        self.stdout.write(self.style.SUCCESS("Фикстуры успешно загружены."))
