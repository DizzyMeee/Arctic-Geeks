from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

# Create your views here
from django.views.generic import CreateView

from account.forms import NewUserForm

class UserCreate(CreateView):
    template_name = 'account/register.html'
    form_class = NewUserForm

    def post(self, request, *args, **kwargs):
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
        return redirect('account:register')

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True

class LogoutView(LogoutView):
    template_name = 'home/home.html'