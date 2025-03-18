from django.core.management import call_command
from django.core.management.base import BaseCommand

from users.models import Payment


class Command(BaseCommand):
    """Очистка базы данных платежей и загрузка сохраненных ранее данных из фикстур в базу данных."""

    help = "Заполнить базу данных платежей из фикстур."

    def handle(self, *args, **kwargs):
        """Функция очистки базы данных и заполнения."""

        Payment.objects.all().delete()

        call_command("loaddata", "fixture/payments_fixture.json")
        self.stdout.write(self.style.SUCCESS("Фикстуры успешно загружены"))
