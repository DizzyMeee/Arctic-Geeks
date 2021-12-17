from django.shortcuts import render

# Create your views here.
def profileView(request):
    return render(request, 'profile-akun.html', {})

def profileAkunView(request):
    return render(request, 'profile-akun.html', {})

def profileRakitView(request):
    return render(request, 'profile-rakit.html', {})