from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import (
    login_register_view,
    LogoutView,
)

app_name = "account"
urlpatterns = [
    path('login-register/', login_register_view, name='login-register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', UserCreate.as_view(), name='register'),
    # path('login/', CustomLoginView.as_view(), name='login'),
]