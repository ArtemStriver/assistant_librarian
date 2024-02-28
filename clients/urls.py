from django.urls import path

from clients import views

urlpatterns = [
    path("", views.view_clients),
    path("create/", views.create, name="create_client"),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]