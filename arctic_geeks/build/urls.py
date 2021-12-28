from os import name
from django.urls import path

from build.views import (
    buildSave,
    buildView,
    buildUpdate,
    buildSuccess,
)

app_name = 'build'
urlpatterns = [
    path('', buildView, name='build'),
    path('<int:id>', buildUpdate, name='build-update'),
    path('success',buildSuccess, name='save-success'),
    path('save/<str:nama>',buildSave, name='build-save'),
    # path('', buildLinkView, name='build-View'),
]