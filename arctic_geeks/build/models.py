from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
from products.models import GPU, CPU, Motherboard, RAM, Disk, PowerSupply, Cooler, Case, Fan
from arctic_geeks.utils import create_shortcode

class Build(models.Model):
    owner = models.CharField(max_length=120, default="")
    gpu = models.ForeignKey(GPU, null=True, blank=True, on_delete=models.DO_NOTHING)
    cpu = models.ForeignKey(CPU, null=True, blank=True, on_delete=models.DO_NOTHING)
    motherboard = models.ForeignKey(Motherboard, null=True, blank=True, on_delete=models.DO_NOTHING)
    ram = models.ForeignKey(RAM, null=True, blank=True, on_delete=models.DO_NOTHING)
    disk = models.ForeignKey(Disk, null=True, blank=True, on_delete=models.DO_NOTHING)
    power_supply = models.ForeignKey(PowerSupply, null=True, blank=True, on_delete=models.DO_NOTHING)
    cooler = models.ForeignKey(Cooler, null=True, blank=True, on_delete=models.DO_NOTHING)
    case = models.ForeignKey(Case, null=True, blank=True, on_delete=models.DO_NOTHING)
    fan = models.ForeignKey(Fan, null=True, blank=True, on_delete=models.DO_NOTHING)

    total_harga = models.PositiveIntegerField(default=0)
    build_title = models.CharField(max_length=120, null=True)
    dibuat = models.DateField(auto_now=True)
        
    def __str__(self):
        return "Build id: %s" %(self.id)

         
# class BuildOwnerList(models.Model):

#     judul = models.ForeignKey(Build, on_delete=models.CASCADE)
    
    

    