from os import name
from django.urls import path

from build.views import (
    buildSave,
    buildView,
    buildUpdate,
)

app_name = 'build'
urlpatterns = [
    path('', buildView, name='build'),
    path('<int:id>', buildUpdate, name='build-update'),
    path('save',buildSave, name='build-save')
    # path('', buildLinkView, name='build-View'),
]