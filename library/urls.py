from django.urls import path

from library import views

"""Настройки маршрутов для взаимодействия с функционалом library."""

urlpatterns = [
    path("", views.view_books),
    path("create/", views.create, name="create_book"),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]
