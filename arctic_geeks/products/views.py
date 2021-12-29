# from typing import List
# from django.db import models
# from django.views.generic import ListView
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.

from .models import GPU, CPU, Motherboard, RAM, Disk, PowerSupply, Cooler, Case, Fan

def gpuComponent(request):
    gpuComponents = GPU.objects.all()
    return render(request, 'products/gpuBrowse.html', {'komponenGPU' : gpuComponents})

def cpuComponentFiltered(request,socket):
    cpuComponents = CPU.objects.filter(socket=socket)
    return render(request, 'products/cpuBrowse.html', {'komponenCPU' : cpuComponents})

def cpuComponent(request):
    cpuComponents = CPU.objects.all()
    return render(request, 'products/cpuBrowse.html', {'komponenCPU' : cpuComponents})
    
def moboComponent(request):
    moboComponents = Motherboard.objects.all()
    return render(request, 'products/moboBrowse.html', {'komponenMobo' : moboComponents})

def moboComponentFiltered(request,ff,socket):
    list_Case = list(Case.objects.values_list('form_factor'))
    for value in list_Case:
        if ff in value:
            if ff == 'ITX':
                moboComponents = Motherboard.objects.filter(form_factor=ff,socket=socket)
            elif ff == 'M-ATX':
                moboComponents = Motherboard.objects.filter(form_factor__in=['M-ATX',ff],socket=socket)
            else:
                moboComponents = Motherboard.objects.filter(socket=socket)
            return render(request, 'products/moboBrowse.html', {'komponenMobo' : moboComponents})
    moboComponents = Motherboard.objects.all()
    return render(request, 'products/moboBrowse.html', {'komponenMobo' : moboComponents})

def moboComponentFiltered1(request,component):
    list_Case = list(Case.objects.values_list('form_factor'))
    list_CPU = list(CPU.objects.values_list('socket'))
    for value in list_Case:
        if component in value:
            if component == 'ITX':
                moboComponents = Motherboard.objects.filter(form_factor=component)
            elif component == 'M-ATX':
                moboComponents = Motherboard.objects.filter(form_factor__in=['M-ATX',component])
            else:
                moboComponents = Motherboard.objects.all()
            return render(request, 'products/moboBrowse.html', {'komponenMobo' : moboComponents})

    for value in list_CPU:
        if component in value:
            print('KetemuCPU')
            moboComponents = Motherboard.objects.filter(socket=component)
            return render(request, 'products/moboBrowse.html', {'komponenMobo' : moboComponents})

    moboComponents = Motherboard.objects.all()
    return render(request, 'products/moboBrowse.html', {'komponenMobo' : moboComponents})

def moboComponentFiltered2(request,socket):
    moboComponents = Motherboard.objects.filter(socket=socket)
    print('socket')
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

def caseComponentFiltered(request,ff):
    list_Motherboard = list(Motherboard.objects.values_list('form_factor'))
    for value in list_Motherboard:
        if ff in value:
            if ff == 'ITX':
                caseComponents = Case.objects.filter(form_factor=ff)
            elif ff == 'M-ATX':
                caseComponents = Case.objects.filter(form_factor__in=['M-ATX',ff])
            else:
                caseComponents = Case.objects.all()
            return render(request, 'products/caseBrowse.html', {'komponenCase' : caseComponents})
    caseComponents = Case.objects.all()
    return render(request, 'products/caseBrowse.html', {'komponenCase' : caseComponents})

def fanComponent(request):
    fanComponents = Fan.objects.all()
    return render(request, 'products/fanBrowse.html', {'komponenFan' : fanComponents})



# def gpuDicoba(request):
    # if request.method == "POST":
    #     gpu_dipilih = request.POST['btn-choose']   
    # komponenGPU = GPU.objects.all()
    # return render(request, 'products/gpunihbos.html', {'komponenGPU' : komponenGPU})