from django.urls import path, re_path

from home.views import (
    HomeView
)

app_name = "home"
urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
]