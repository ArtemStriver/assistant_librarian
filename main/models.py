from django.db import models


class Book(models.Model):
    title = models.CharField()
    # TODO можно вынести жанр и автора в отдельные таблицы и через FK связать их
    author = models.CharField()
    genre = models.CharField()
    count = models.IntegerField()

    class Meta:
        db_table = 'book'


class BookInfo(models.Model):
    book_id = models.ForeignKey('Book',
                                related_name='book_client',
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    client_id = models.ForeignKey('Client',
                                  related_name='book_client',
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  null=True)
    take_date = models.DateField()
    return_date = models.DateField()

    class Meta:
        db_table = 'book_info'


class Client(models.Model):
    name = models.CharField()
    address = models.CharField()
    visit_date = models.DateField()

    class Meta:
        db_table = 'client'
