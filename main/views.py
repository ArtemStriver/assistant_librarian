from django.shortcuts import render


def index(request):
    """Функция отображения главного меню."""
    return render(request, "index.html")
