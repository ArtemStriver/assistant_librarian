from datetime import datetime

from django.db import models


class Client(models.Model):
    name = models.CharField()
    address = models.CharField()
    phone = models.CharField()
    visit_date = models.DateField(default=datetime.utcnow())

    class Meta:
        db_table = 'client'
