from django.urls import path

from products.views import (
    GPUBrowseView,
)
app_name = "products"
urlpatterns = [
    path('gpu/', GPUBrowseView.as_view(), name='gpu'),
]