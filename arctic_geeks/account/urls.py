from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import (
    login_register_view,
    logoutView,
)

app_name = "account"
urlpatterns = [
    path('login-register/', login_register_view, name='login-register'),
    path('logout/', logoutView, name='logout'),
]