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
    fanComponent,
    cpuComponentFiltered,
    caseComponentFiltered,
    moboComponentFiltered,
    moboComponentFiltered1,
)
app_name = "products"
urlpatterns = [
    path('gpu/', gpuComponent, name='gpu'),
    path('cpu/', cpuComponent, name='cpu'),
    path('cpu/<str:socket>', cpuComponentFiltered, name='cpuFilter'),
    path('mobo/', moboComponent, name='mobo'),
    path('mobo/<str:ff>/<str:socket>', moboComponentFiltered, name='moboFilter'),
    path('mobo/<str:component>', moboComponentFiltered1, name='moboFilter_satu'),
    path('ram/', ramComponent, name='ram'),
    path('disk/', diskComponent, name='disk'),
    path('psu/', psuComponent, name='psu'),
    path('cooler/', coolerComponent, name='cooler'),
    path('case/', caseComponent, name='case'),
    path('case/<str:ff>', caseComponentFiltered, name='caseFilter'),
    path('fan/', fanComponent, name='fan'),
]