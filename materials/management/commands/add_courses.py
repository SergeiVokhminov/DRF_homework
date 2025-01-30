from django.core.management import call_command
from django.core.management.base import BaseCommand

from materials.models import Course


class Command(BaseCommand):
    """Очистка базы данных курсов и загрузка сохраненных ранее данных из фикстур в базу данных."""

    help = "Заполнить базу данных курсов из фикстур."

    def handle(self, *args, **kwargs):
        """Функция очистки базы данных и заполнения."""
        Course.objects.all().delete()

        call_command("loaddata", "fixture/courses_fixture.json")
        self.stdout.write(self.style.SUCCESS("Фикстуры успешно загружены."))
