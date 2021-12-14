from django.db import models
from django.utils.text import slugify

from polymorphic.models import PolymorphicModel

# Create your models here.
class Komponen(PolymorphicModel):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=30)
    nama_komponen = models.CharField(max_length=250, default="")
    harga = models.PositiveIntegerField()
    gambar = models.ImageField(upload_to='images/', blank=True)
    link_tokopedia = models.URLField(blank=True)
    link_shopee = models.URLField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return str(self.id)

class GPU(Komponen):
    manufaktur = models.CharField(max_length=30)
    series = models.CharField(max_length=60)

class CPU(Komponen):
    cores = models.PositiveIntegerField(default=2)
    threads = models.PositiveIntegerField(default=4)
    watts = models.PositiveIntegerField(default=0)
    socket = models.CharField(max_length=15)

class Motherboard(Komponen):
    manufaktur = models.CharField(max_length=30)
    socket = models.CharField(max_length=15)
    chipset = models.CharField(max_length=40)
    form_factor = models.CharField(max_length=20)

class RAM(Komponen):
    kapasitas = models.PositiveIntegerField(default=2)
    tipe_channel = models.CharField(max_length=100)
    kecepatan = models.PositiveIntegerField(default=2133)

class Disk(Komponen):
    kapasitas = models.CharField(max_length=10)
    tipe = models.CharField(max_length=20)
    form_factor = models.CharField(max_length=20)

class PowerSupply(Komponen):
    daya = models.PositiveIntegerField(default=0)
    efisiensi = models.CharField(max_length=50)

class Cooler(Komponen):
    tipe = models.CharField(max_length=50)

class Case(Komponen):
    form_factor = models.CharField(max_length=20)

class Fan(Komponen):
    rpm_max = models.PositiveIntegerField(default=0)