# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
# from django.http.response import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib import auth
# from django.contrib import messages

from account.forms import CreateUserForm
# from django.views.generic import CreateView

# from account.forms import NewUserForm

# Create your views here
def login_register_view(request):
    form = CreateUserForm()

    if request.method == "POST":
        if request.POST.get('submit') == 'register':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('account:login-register')

        elif request.POST.get('submit') == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('home:home')
            
    context = {'form': form}
    return render(request, 'account/login-register.html', context)

class LogoutView(LogoutView):
    template_name = 'home/home.html'

# def login_register_view(request):
#     if request.method == "POST":
#         if request.POST.get('submit') == 'register':
#             username = request.POST['username']
#             email = request.POST['email']
#             password1 = request.POST['password1']
#             password2 = request.POST['password2']

#             if password1 == password2:
#                 if User.objects.filter(username=username).exists():
#                     messages.warning(request, "Username already taken.")
#                     return render(request, 'account/login-register.html')
#                 elif User.objects.filter(email=email).exists():
#                     messages.warning(request, "Email already taken.")
#                     return render(request, 'account/login-register.html')
#                 else:
#                     user = User.objects.create_user(username=username, email=email, password=password1)
#                     user.save()
#                     messages.success(request, "User created successfull.")
#                     return redirect('account:login-register')
#                     return HttpResponse('')
#             else:
#                 messages.warning(request, 'Password did not match.')
#                 return render(request, 'account/login-register.html')

#         elif request.POST.get('submit') == 'login':
#             user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
#             if user is not None:
#                 auth.login(request, user)
#                 return redirect('home:home')
#             else:
#                 return render(request, 'account/login-register.html', {'error': 'Username or password is incorrect!'})
#     else:
#         return render(request, 'account/login-register.html')

# class UserCreate(CreateView):
#     template_name = 'account/register.html'
#     form_class = NewUserForm

#     def post(self, request, *args, **kwargs):
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('account:login')
#         return redirect('account:register')

# class CustomLoginView(LoginView):
#     template_name = 'account/login.html'
#     redirect_authenticated_user = True

# class LogoutView(LogoutView):
#     template_name = 'home/home.html'