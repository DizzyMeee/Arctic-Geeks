from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

from django.contrib.auth.models import User

from .models import Build
from products.models import Komponen, GPU, CPU, Motherboard, RAM, Disk, PowerSupply, Cooler, Case, Fan

# Create your views here.
def buildView(request):
    print("view")
    try:
        build_id = request.session['build_id']
        print("try")
        print(build_id)
    except:
        print("kosong")
        build_id = None
    
    if build_id:
        build = Build.objects.get(id=build_id)
        if build:
            print("??")
            context = {"build": build}
        else:
            print("!!")
            context = {"empty": True}
    else:
        print("asu")
        context = {"empty": True}
    template = 'build/coba-build.html'
    return render(request, template, context)

def buildUpdate(request, id):
    # build = Build.objects.all()[0]
    # new_total = 0
    print("update")
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
        request.session.modified = True
        build_id = request.session['build_id']
        print("try")
        print(build_id)
    except:
        new_build = Build()
        print("except")
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
    
    if build.gpu is None:
        harga_gpu = 0
    else:
        harga_gpu = build.gpu.harga
    
    if build.cpu is None:
        harga_cpu = 0
    else:
        harga_cpu = build.cpu.harga
    
    if build.motherboard is None:
        harga_mobo = 0
    else:
        harga_mobo = build.motherboard.harga
    
    if build.ram is None:
        harga_ram = 0
    else:
        harga_ram = build.ram.harga
    
    if build.disk is None:
        harga_disk = 0
    else:
        harga_disk = build.disk.harga
    
    if build.power_supply is None:
        harga_psu = 0
    else:
        harga_psu = build.power_supply.harga
    
    if build.cooler is None:
        harga_cooler = 0
    else:
        harga_cooler = build.cooler.harga
    
    if build.case is None:
        harga_case = 0
    else:
        harga_case = build.case.harga
    
    if build.fan is None:
        harga_fan = 0
    else:
        harga_fan = build.fan.harga
    
    build.total_harga = harga_gpu + harga_cpu + harga_mobo + harga_ram + harga_psu + harga_disk + harga_cooler + harga_case + harga_fan
    
    build.save()
    return HttpResponseRedirect(reverse("build:build"))


def buildSave(request):
    print('wtf')
    try:
        build_id = request.session['build_id']
    except:
        build_id = None
        
    if build_id:
        print("berhasil")
        build = Build.objects.get(id=build_id)
        build.owner = request.user.username
        build.build_title = 'Testing RAKIT'
        print(build.owner)
        build.save()
    del request.session['build_id']
    return HttpResponseRedirect(reverse("build:build"))

def viewExistingBuild(request):
    pass
    


# def buildView(request):
#     return render(request, 'build/build.html', {})

# class BuildView(View):
#     def render(self, request):
#         return render(request, 'build/build.html', {'component_list': self.component_list})
    
#     def get(self, request, *args, **kwargs):
#         self.component_list = Build.get_component_dict()

#         return self.render(request)