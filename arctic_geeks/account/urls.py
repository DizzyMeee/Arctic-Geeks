from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import (
    login,
    register,
    logoutView,
)

app_name = "account"
urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout/', logoutView, name='logout'),
]