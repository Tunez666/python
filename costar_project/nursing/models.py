from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Customer(models.Model):
    """Физлица - покупатели билетов"""
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    birth_date = models.DateField(verbose_name='Дата рождения')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class MovieSession(models.Model):
    """Сеансы фильмов"""
    title = models.CharField(max_length=200, verbose_name='Название фильма')
    start_time = models.DateTimeField(verbose_name='Время начала')
    end_time = models.DateTimeField(verbose_name='Время окончания')

    class Meta:
        verbose_name = 'Киносеанс'
        verbose_name_plural = 'Киносеансы'

    def __str__(self):
        return f"{self.title} ({self.start_time.strftime('%d.%m.%Y %H:%M')})"


class Seat(models.Model):
    """Места в зале"""
    number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        unique=True,
        verbose_name='Номер места'
    )

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return f"Место {self.number}"


class Ticket(models.Model):
    """Проданные билеты"""
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='tickets',
        verbose_name='Покупатель'
    )
    session = models.ForeignKey(
        MovieSession,
        on_delete=models.CASCADE,
        related_name='tickets',
        verbose_name='Сеанс'
    )
    seat = models.ForeignKey(
        Seat,
        on_delete=models.CASCADE,
        related_name='tickets',
        verbose_name='Место'
    )
    purchase_time = models.DateTimeField(auto_now_add=True, verbose_name='Время покупки')

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        unique_together = [['session', 'seat']]  # Одно место - один билет на сеанс

    def __str__(self):
        return f"Билет #{self.id} ({self.customer.last_name})"
# Create your models here.
