from django.urls import re_path
from . import views

app_name = "info"

urlpatterns = [
    re_path("weather/", views.weatherView, name="weather"),
    re_path("soil/", views.soilView, name="soil"),
    re_path("set_reminder/", views.setReminderView, name="set_reminder"),
    re_path("get_reminder/", views.getReminderView, name="get_reminder"),
]