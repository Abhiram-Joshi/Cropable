from django.urls import re_path
from .views import *

app_name = "forum"

urlpatterns = [
    re_path('^$', home, name='home'),
    re_path('^addInForum/', addInForum, name='addInForum'),
    re_path('^addInDiscussion/', addInDiscussion, name='addInDiscussion'),
]