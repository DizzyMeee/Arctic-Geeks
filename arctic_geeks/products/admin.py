from django.contrib import admin

# Register your models here.
from .models import GPU, CPU, Motherboard, RAM, Disk, PowerSupply, Cooler, Case, Fan

admin.site.register(GPU)
admin.site.register(CPU)
admin.site.register(Motherboard)
admin.site.register(RAM)
admin.site.register(Disk)
admin.site.register(PowerSupply)
admin.site.register(Cooler)
admin.site.register(Case)
admin.site.register(Fan)