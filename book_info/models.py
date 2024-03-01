from django.db import models

from clients.models import Client
from library.models import Book


class BookInfo(models.Model):
    """
    Модель таблицы с информацией о факте взятия и возврата книг читателями.
    """
    book_id = models.ForeignKey(Book,
                                related_name='book_client',
                                on_delete=models.CASCADE,
                                blank=True,
                                null=False)
    client_id = models.ForeignKey(Client,
                                  related_name='book_client',
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  null=False)
    take_date = models.DateField()
    return_date = models.DateField(null=True)

    class Meta:
        db_table = 'book_info'
