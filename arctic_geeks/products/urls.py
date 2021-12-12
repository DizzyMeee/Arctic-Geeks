from django.urls import path

from products.views import (
    GPUBrowseView,gpuComponent
)
app_name = "products"
urlpatterns = [
    path('gpu/', gpuComponent, name='gpu'),
]