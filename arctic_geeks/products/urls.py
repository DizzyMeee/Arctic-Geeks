from django.urls import path

from products.views import (
    gpuComponent,
    cpuComponent,
    moboComponent,
    ramComponent,
    diskComponent,
    psuComponent,
    coolerComponent,
    caseComponent,
    fanComponent
)
app_name = "products"
urlpatterns = [
    path('gpu/', gpuComponent, name='gpu'),
    path('cpu/', cpuComponent, name='cpu'),
    path('mobo/', moboComponent, name='mobo'),
    path('ram/', ramComponent, name='ram'),
    path('disk/', diskComponent, name='disk'),
    path('psu/', psuComponent, name='psu'),
    path('cooler/', coolerComponent, name='cooler'),
    path('case/', caseComponent, name='case'),
    path('fan/', fanComponent, name='fan'),
]