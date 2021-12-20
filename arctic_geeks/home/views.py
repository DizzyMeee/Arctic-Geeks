from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def homeView(request):
    return render(request, 'home/home.html', {})

# class HomeView(TemplateView):
#     template_name = 'home/home.html'