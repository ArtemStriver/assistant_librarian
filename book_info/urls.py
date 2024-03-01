from django.urls import path

from book_info import views

"""Настройки маршрутов для взаимодействия с функционалом book_info."""

urlpatterns = [
    path("", views.view_book_info),
    path("take_book/", views.take_book, name="take_book"),
    path("return_book/<int:id>/", views.return_book),
]
