from django.urls import path

from . import views

# namespace para usar {% url 'polls:detail' ... %} sin chocar con otras apps
app_name = "polls"

# rutas propias de la app polls
urlpatterns = [
    # ej: /polls/
    path("", views.index, name="index"),
    # ej: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ej: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ej: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
