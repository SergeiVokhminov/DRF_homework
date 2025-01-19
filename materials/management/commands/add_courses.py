from django.core.management import call_command
from django.core.management.base import BaseCommand

from materials.models import Course


class Command(BaseCommand):
    help = "Fill the database from fixture"

    def handle(self, *args, **kwargs):
        Course.objects.all().delete()

        call_command("loaddata", "fixture/courses_fixture.json")
        self.stdout.write(self.style.SUCCESS("Фикстуры успешно загружены"))
