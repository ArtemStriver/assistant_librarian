from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotFound

from book_info.models import BookInfo
from clients.models import Client
from library.models import Book


def view_book_info(request):
    book_info = BookInfo.objects.all()
    return render(request, "book_info.html", {"book_info": book_info})


def take_book(request):

    if request.method == "POST":
        try:
            book_info = BookInfo()
            book_id = int(request.POST.get("book_id"))
            client_id = int(request.POST.get("client_id"))

            book = Book.objects.get(id=book_id)
            client = Client.objects.get(id=client_id)

            if book.book_count == 0:
                return HttpResponseBadRequest(
                    "<h2>Книг нет в наличии, попробуйте взять <a href='/book_info'>другую</a></h2>"
                )
            book_info.book_id = book
            book_info.client_id = client
            book_info.take_date = request.POST.get("take_date")

            book.book_count = book.book_count - 1
            client.visit_date = request.POST.get("take_date")

            book.save()
            client.save()
            book_info.save()
            return HttpResponseRedirect("/book_info")
        except Exception as exc:
            print(exc)
            return HttpResponseBadRequest(
                "<h2>Ошибочные данные, попробуйте <a href='/book_info'>еще раз</a></h2>"
            )

    return render(request, "take_book_page.html")


def return_book(request, id):
    try:
        book_info = BookInfo.objects.get(id=id)

        if request.method == "POST":
            book_info.return_date = request.POST.get("return_date")
            book = Book.objects.get(id=book_info.book_id.id)
            client = Client.objects.get(id=book_info.client_id.id)

            book.book_count = book.book_count + 1
            client.visit_date = request.POST.get("return_date")

            book.save()
            client.save()
            book_info.save()
            return HttpResponseRedirect("/book_info")
        else:
            return render(request, "return_book_page.html", {"book_info": book_info})
    except BookInfo.DoesNotExist:
        return HttpResponseNotFound("<h2>not found</h2>")
