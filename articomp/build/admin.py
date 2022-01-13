from django.contrib import admin

# Register your models here.
from .models import Build

admin.site.register(Build)
# class buildOrder(admin.ModelAdmin):
#     list_display = ('user','id','shortcode','items')
# admin.site.register(Build,)
