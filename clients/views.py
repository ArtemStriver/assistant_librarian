from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

from clients.models import Client


def view_clients(request):
    """Функция отображения меню clients."""
    clients = Client.objects.all()
    return render(request, "clients.html", {"clients": clients})


def create(request):
    """Функция по добавлению нового читателя."""
    if request.method == "POST":
        client = Client()
        client.client_name = request.POST.get("client_name")
        client.address = request.POST.get("address")
        client.phone = request.POST.get("phone")
        client.save()
        return HttpResponseRedirect("/clients")

    return render(request, "add_client.html")


def edit(request, id):
    """Функция по изменению данных читателя."""
    try:
        client = Client.objects.get(id=id)

        if request.method == "POST":
            client.client_name = request.POST.get("client_name")
            client.address = request.POST.get("address")
            client.phone = request.POST.get("phone")
            client.save()
            return HttpResponseRedirect("/clients")
        else:
            return render(request, "edit_client.html", {"client": client})
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2>not found</h2>")


def delete(request, id):
    """Функция по удалению читателя."""
    try:
        client = Client.objects.get(id=id)
        client.delete()
        return HttpResponseRedirect("/clients")
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2>not found</h2>")
