from django.urls import re_path
from . import views

urlpatterns = [
    re_path("weather/", views.weatherView, name="weather"),
]