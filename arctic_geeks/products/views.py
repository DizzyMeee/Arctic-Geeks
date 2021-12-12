from typing import List
from django.db import models
from django.views.generic import ListView
from django.shortcuts import render, redirect
# Create your views here.

from .models import GPU, CPU, Motherboard, RAM, Disk, PowerSupply, Cooler, Case, Fan

class AbstractComponentBrowseView(ListView):
    context_object_name = 'components'
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

class GPUBrowseView(AbstractComponentBrowseView):
    model = GPU
    template_name = 'products/gpuBrowse.html'
    title = 'Pilih Graphic Card (GPU)'
    
    
def gpuComponent(request):
    gpuComponents = GPU.objects.all()
    return render(request, 'products/componentBrowse.html', {'componentsGPU' : gpuComponents})