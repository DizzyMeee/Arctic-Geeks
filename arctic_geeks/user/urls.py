from django.urls import path

from user.views import(
    deleteBuild,
    profileView,
    userBuildView,
    viewExistingBuild
)



app_name = 'user'
urlpatterns = [
    path('', profileView, name='profile'),
    path('builds/', userBuildView, name='builds'),
    path('view/<id>', viewExistingBuild,name='viewBuild'),
    path('delete/<id>', deleteBuild, name='deleteBuild'),
]