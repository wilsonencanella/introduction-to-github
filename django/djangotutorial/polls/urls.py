from django.urls import path

from . import views

# namespace para usar {% url 'polls:detail' ... %} sin chocar con otras apps
app_name = "polls"

# rutas propias de la app polls
urlpatterns = [
    # ej: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ej: /polls/5/  (las vistas genericas esperan que se llame pk)
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ej: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ej: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
