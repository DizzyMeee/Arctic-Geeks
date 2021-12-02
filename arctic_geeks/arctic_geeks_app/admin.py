from django.contrib import admin
from .models import JenisKomponen, Komponen, JenisInfo, InfoKomponen

# Register your models here.
admin.site.register(JenisKomponen)
admin.site.register(Komponen)
admin.site.register(JenisInfo)
admin.site.register(InfoKomponen)