from django.contrib import admin

from book_info.models import BookInfo

"""Настройки админ панели для работы с book_info."""


@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    pass
