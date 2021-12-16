from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

from .models import Build
from products.models import Komponen, GPU, CPU, Motherboard, RAM, Disk, PowerSupply, Cooler, Case, Fan

# Create your views here.
def buildView(request):
    try:
        build_id = request.session['build_id']
    except:
        build_id = None
    
    if build_id:
        build = Build.objects.get(id=build_id)
        context = {"build": build}
    else:
        context = {"empty": True}
    template = 'build/coba-build.html'
    return render(request, template, context)

def buildUpdate(request, id):
    # build = Build.objects.all()[0]
    list_gpu = GPU.objects.all()
    list_cpu = CPU.objects.all()
    list_mobo = Motherboard.objects.all()
    list_ram = RAM.objects.all()
    list_disk = Disk.objects.all()
    list_psu = PowerSupply.objects.all()
    list_cooler = Cooler.objects.all()
    list_case = Case.objects.all()
    list_fan = Fan.objects.all()
    try:
        build_id = request.session['build_id']
    except:
        new_build = Build()
        new_build.save()
        request.session['build_id'] = new_build.id
        build_id = new_build.id
    
    build = Build.objects.get(id=build_id)

    try:
        komponen = Komponen.objects.get(id=id)
    except Komponen.DoesNotExist:
        pass
    except:
        pass

    if komponen in list_gpu:
        if komponen == build.gpu:
            build.gpu = None
        else:
            build.gpu = komponen
        
    if komponen in list_cpu:
        if komponen == build.cpu:
            build.cpu = None
        else:
            build.cpu = komponen
    
    if komponen in list_mobo:
        if komponen == build.motherboard:
            build.motherboard = None
        else:
            build.motherboard = komponen
    
    if komponen in list_ram:
        if komponen == build.ram:
            build.ram = None
        else:
            build.ram = komponen

    if komponen in list_disk:
        if komponen == build.disk:
            build.disk = None
        else:
            build.disk = komponen

    if komponen in list_psu:
        if komponen == build.power_supply:
            build.power_supply = None
        else:
            build.power_supply = komponen

    if komponen in list_cooler:
        if komponen == build.cooler:
            build.cooler = None
        else:
            build.cooler = komponen
    
    if komponen in list_case:
        if komponen == build.case:
            build.case = None
        else:
            build.case = komponen
    if komponen in list_fan:
        if komponen == build.fan:
            build.fan = None
        else:
            build.fan = komponen
    
    build.save()
    return HttpResponseRedirect(reverse("build:build"))


# def buildView(request):
#     return render(request, 'build/build.html', {})

# class BuildView(View):
#     def render(self, request):
#         return render(request, 'build/build.html', {'component_list': self.component_list})
    
#     def get(self, request, *args, **kwargs):
#         self.component_list = Build.get_component_dict()

#         return self.render(request)