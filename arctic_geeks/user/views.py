from django.shortcuts import render
from build.models import Build
# Create your views here.
def profileView(request, username):
    context = {}
    return render(request, 'user/profile-akun.html', context)

def userBuildView(request, username):
    build = Build.objects.filter(owner=request.user.username)
    print(build)
    context = {"build": build}
    return render(request, 'user/profile-rakit.html', context)

def deleteBuild(request):
    pass