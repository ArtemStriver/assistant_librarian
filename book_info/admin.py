from django.contrib import admin

from book_info.models import BookInfo


@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    pass
