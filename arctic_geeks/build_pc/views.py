from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Build_PCView(TemplateView):
    template_name = 'menu-rakit.html'