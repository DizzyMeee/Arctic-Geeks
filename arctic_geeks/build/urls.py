from django.urls import path

from build.views import (
    buildView,
    buildUpdate,
)

app_name = 'build'
urlpatterns = [
    path('', buildView, name='build'),
    path('<int:id>', buildUpdate, name='build-update'),
]