from django.urls import re_path

from . import views

app_name = "detector"

urlpatterns = [
    re_path(r"^upload-image/$", views.addCropImage, name="add_crop_image"),
    # re_path(r"^predict/(?P<file_path>\w+)/(?P<id>\d+)/", views.predict, name="predict_disease"),
    re_path(r"^predict/", views.predict, name="predict_disease"),
]