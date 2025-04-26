from django.core.management.base import BaseCommand
from nursing.models import MovieSession, Seat
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Заполняет БД начальными данными (места и сеансы)'

    def handle(self, *args, **options):
        # Очистка старых данных
        Seat.objects.all().delete()
        MovieSession.objects.all().delete()

        # Создаем 100 мест
        seats = [Seat(number=i) for i in range(1, 101)]
        Seat.objects.bulk_create(seats)

        # Создаем тестовые сеансы
        now = datetime.now()
        MovieSession.objects.bulk_create([
            MovieSession(
                title="Avatar 2",
                start_time=now + timedelta(hours=2),
                end_time=now + timedelta(hours=4)
            ),
            MovieSession(
                title="Duna",
                start_time=now + timedelta(hours=5),
                end_time=now + timedelta(hours=8)
            ),
            MovieSession(
                title="Forsage 10",
                start_time=now + timedelta(days=1, hours=3),
                end_time=now + timedelta(days=1, hours=5)
            )
        ])

        self.stdout.write(self.style.SUCCESS('Создано 100 мест и 3 сеанса!'))