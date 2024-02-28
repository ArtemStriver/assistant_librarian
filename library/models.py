from django.db import models


class Book(models.Model):
    title = models.CharField()
    # TODO можно вынести жанр и автора в отдельные таблицы и через FK связать их
    author = models.CharField()
    genre = models.CharField()
    count = models.IntegerField()

    class Meta:
        db_table = 'book'
