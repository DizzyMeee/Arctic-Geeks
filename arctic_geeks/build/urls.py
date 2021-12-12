from django.urls import path

from build.views import (
    buildView,
)

app_name = 'build'
urlpatterns = [
    path('', buildView, name='build'),
]