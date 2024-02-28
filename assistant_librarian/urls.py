from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('library/', include("library.urls")),
    path('clients/', include("clients.urls")),
    path('book_info/', include("book_info.urls")),
    path('reports/', include("reports.urls")),
]
