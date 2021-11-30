from django.contrib import admin

# Register your models here.
from .models import TagComponent, Component

admin.site.register(TagComponent)
admin.site.register(Component)