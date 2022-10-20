from django.urls import re_path

from . import views

app_name = "account"

urlpatterns = [
    re_path(r"^signup/$", views.user_signup, name="user_signup"),
    re_path(r"^login/$", views.user_login, name="user_login"),
    re_path(r"^logout/$", views.user_logout, name="user_logout"),
]