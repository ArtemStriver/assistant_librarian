from django.contrib import admin

from main.models import Book, Client, BookInfo


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    pass
