from django.urls import path
from . import views

app_name = "chart"
urlpatterns = [
    path("", views.index, name="index"),
    path("schools/", views.schools, name="schools"),
    path("matches/", views.matches, name="matches")
]
