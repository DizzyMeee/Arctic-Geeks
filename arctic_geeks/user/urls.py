from django.urls import path

from user.views import(
    profileView,
    userBuildView
)



app_name = 'user'
urlpatterns = [
    path('', profileView, name='profile'),
    path('builds/', userBuildView, name='builds'),
]