from django.db import models


class Book(models.Model):
    """
    Модель таблицы с книгами.

    Возможное улучшение:
    Можно вынести жанр и автора в отдельные таблицы
    и через FK связать их, для оптимизации запросов в БД.
    """
    title = models.CharField()
    author = models.CharField()
    genre = models.CharField()
    book_count = models.IntegerField()

    class Meta:
        db_table = 'book'
