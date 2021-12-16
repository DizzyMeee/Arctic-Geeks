from django.db import models

# Create your models here.
from products.models import GPU, CPU, Motherboard, RAM, Disk, PowerSupply, Cooler, Case, Fan

class Build(models.Model):
    gpu = models.ForeignKey(GPU, null=True, blank=True, on_delete=models.DO_NOTHING)
    cpu = models.ForeignKey(CPU, null=True, blank=True, on_delete=models.DO_NOTHING)
    motherboard = models.ForeignKey(Motherboard, null=True, blank=True, on_delete=models.DO_NOTHING)
    ram = models.ForeignKey(RAM, null=True, blank=True, on_delete=models.DO_NOTHING)
    disk = models.ForeignKey(Disk, null=True, blank=True, on_delete=models.DO_NOTHING)
    power_supply = models.ForeignKey(PowerSupply, null=True, blank=True, on_delete=models.DO_NOTHING)
    cooler = models.ForeignKey(Cooler, null=True, blank=True, on_delete=models.DO_NOTHING)
    case = models.ForeignKey(Case, null=True, blank=True, on_delete=models.DO_NOTHING)
    fan = models.ForeignKey(Fan, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Build id: %s" %(self.id)