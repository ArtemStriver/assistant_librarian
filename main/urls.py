from django.urls import path

from main import views

"""Настройки маршрута для главного меню."""

urlpatterns = [
    path('', views.index),
]
