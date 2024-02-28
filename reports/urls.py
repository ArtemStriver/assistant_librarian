from django.urls import path

from library import views

urlpatterns = [
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]
