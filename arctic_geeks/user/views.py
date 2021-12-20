from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse
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

def deleteBuild(request, username, id):
    build = Build.objects.get(id=id)
    build.delete()
    return redirect('/user/'+ username + '/builds')

def viewExistingBuild(request,username,id):
    try:
        request.session.modified = True
        request.session['build_id'] = id
        print('viewwtf')
        build = Build.objects.get(id=id)
        build.save()
    except:
        pass
    return HttpResponseRedirect(reverse("build:build"))