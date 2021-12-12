# from typing import List
# from django.db import models
# from django.views.generic import ListView
from django.shortcuts import render, redirect
# Create your views here.

from .models import GPU, CPU, Motherboard, RAM, Disk, PowerSupply, Cooler, Case, Fan

def gpuComponent(request):
    gpuComponents = GPU.objects.all()
    return render(request, 'products/gpuBrowse.html', {'komponenGPU' : gpuComponents})

def cpuComponent(request):
    cpuComponents = CPU.objects.all()
    return render(request, 'products/cpuBrowse.html', {'komponenCPU' : cpuComponents})

def moboComponent(request):
    moboComponents = Motherboard.objects.all()
    return render(request, 'products/moboBrowse.html', {'komponenMobo' : moboComponents})

def ramComponent(request):
    ramComponents = RAM.objects.all()
    return render(request, 'products/ramBrowse.html', {'komponenRAM' : ramComponents})

def diskComponent(request):
    diskComponents = Disk.objects.all()
    return render(request, 'products/diskBrowse.html', {'komponenDisk' : diskComponents})

def psuComponent(request):
    psuComponents = PowerSupply.objects.all()
    return render(request, 'products/psuBrowse.html', {'komponenPSU' : psuComponents})

def coolerComponent(request):
    coolerComponents = Cooler.objects.all()
    return render(request, 'products/coolerBrowse.html', {'komponenCooler' : coolerComponents})

def caseComponent(request):
    caseComponents = Case.objects.all()
    return render(request, 'products/caseBrowse.html', {'komponenCase' : caseComponents})

def fanComponent(request):
    fanComponents = Fan.objects.all()
    return render(request, 'products/fanBrowse.html', {'komponenFan' : fanComponents})

# class AbstractComponentBrowseView(ListView):
#     context_object_name = 'components'
#     title = None

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = self.title

#         return context

# class GPUBrowseView(AbstractComponentBrowseView):
#     model = GPU
#     template_name = 'products/gpuBrowse.html'
#     title = 'Pilih Graphic Card (GPU)'