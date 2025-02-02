from django.contrib import admin
from .models import Game, Buyer


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Фильтрация по полям size и cost
    list_filter = ('size', 'cost')

    # Отображение полей title, cost и size при отображении всех полей списком
    list_display = ('title', 'cost', 'size')

    # Поиск по полю title
    search_fields = ('title',)

    # Ограничение кол-ва записей до 20
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    # Фильтрация по полям balance и age
    list_filter = ('balance', 'age')

    # Отображение полей name, balance и age при отображении всех полей списком
    list_display = ('name', 'balance', 'age')

    # Поиск по полю name
    search_fields = ('name',)

    # Ограничение кол-ва записей до 30
    list_per_page = 30

    # Поле balance доступно только для чтения
    readonly_fields = ('balance',)