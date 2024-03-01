from django.urls import path

from reports import views

"""Настройки маршрутов для взаимодействия с функционалом reports."""

urlpatterns = [
    path("", views.view_reports),
    path("report1/", views.report1),
    path("report2/", views.report2),
    path("report3/", views.report3),
    path("report4/", views.report4),
    path("report5/", views.report5),
    path("report6/", views.report6),
    path("report7/", views.report7),
]
