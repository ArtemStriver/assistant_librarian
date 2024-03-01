from django.contrib import admin

from clients.models import Client

"""Настройки админ панели для работы с client."""


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
