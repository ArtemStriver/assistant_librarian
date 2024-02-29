from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

from library.models import Book


def view_books(request):
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM main_book")
    #     books = cursor.fetchall()
    # print(books, "OK")

    books = Book.objects.all()
    return render(request, "books.html", {"books": books})


def create(request):
    if request.method == "POST":
        book = Book()
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.genre = request.POST.get("genre")
        book.book_count = request.POST.get("book_count")
        book.save()
        return HttpResponseRedirect("/library")

    return render(request, "add_book.html")


def edit(request, id):
    try:
        book = Book.objects.get(id=id)

        if request.method == "POST":
            book.title = request.POST.get("title")
            book.author = request.POST.get("author")
            book.genre = request.POST.get("genre")
            book.book_count = request.POST.get("book_count")
            book.save()
            return HttpResponseRedirect("/library")
        else:
            return render(request, "edit_book.html", {"book": book})
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>not found</h2>")


def delete(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return HttpResponseRedirect("/library")
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>not found</h2>")
