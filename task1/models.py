from django.db import models
from decimal import Decimal

class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Имя покупателя (уникальное)
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
    age = models.PositiveIntegerField()  # Возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов игры
    description = models.TextField()  # Описание
    age_limited = models.BooleanField(default=False)  # Ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer, related_name='games')  # Связь ManyToMany с Buyer

    def __str__(self):
        return self.title