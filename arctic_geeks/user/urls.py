from django.urls import path, re_path
from user.views import profileView, profileAkunView, profileRakitView
app_name = "profile"
urlpatterns = [
    re_path(r'^$', profileView, name='profile'),
    path('akun/', profileAkunView, name='akun'),
    path('rakit/', profileRakitView, name='rakit'),
]