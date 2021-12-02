from django.db import models

#Create your models here.
class JenisKomponen(models.Model): # mobo, processor etc.
    id_jenis_komponen = models.AutoField(primary_key=True)
    jenis_komponen = models.CharField(max_length=100)

class Komponen(models.Model):
    id_komponen = models.AutoField(primary_key=True)
    nama_komponen = models.CharField(max_length=150)
    jenis_komponen = models.ForeignKey(JenisKomponen, on_delete=models.CASCADE)
    harga_komponen = models.DecimalField(decimal_places=2, max_digits=11)
    gambar_komponen = models.ImageField(upload_to='images/')

class JenisInfo(models.Model): # manufacture, core, thread etc. 
    id_jenis_info = models.AutoField(primary_key=True)
    jenis_info = models.CharField(max_length=120)

class InfoKomponen(models.Model):
    id_info_komponen = models.AutoField(primary_key=True)
    nama_komponen = models.ForeignKey(Komponen, db_column='id_komponen', on_delete=models.CASCADE)
    jenis_info = models.ForeignKey(JenisKomponen, db_column='id_jenis_komponen', on_delete=models.CASCADE)
    value = models.CharField(max_length=120)