from django.urls import path

from . import views

# rutas propias de la app polls
urlpatterns = [
    path("", views.index, name="index"),
]
