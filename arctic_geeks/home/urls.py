from django.urls import path, re_path

from home.views import (
    homeView
)



app_name = "home"
urlpatterns = [
    re_path(r'^$', homeView, name='home'),
    
]