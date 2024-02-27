from django.urls import path

from main import views

urlpatterns = [
    path('', views.index),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]
