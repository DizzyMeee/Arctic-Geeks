from django.urls import path

from account.views import (
    UserCreate,
    CustomLoginView,
    LogoutView
)

app_name = "account"
urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]