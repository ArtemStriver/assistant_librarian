from django.contrib import admin

from library.models import Book

"""Настройки админ панели для работы с book."""


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
