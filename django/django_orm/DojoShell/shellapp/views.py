from django.shortcuts import redirect, render,HttpResponse
from shellapp.models import *
# Create your views here.
def index(request):
    context={
        'all':Dojo.objects.all()
    }
    return render(request,"index.html",context)
def addDojo(request):
    Dojo.objects.create(name=request.POST['name'],city=request.POST['city'],state=request.POST['state'])
    return redirect('/')
def addNinja(request):
    print(request.POST['dojo'])
    x=Dojo.objects.get(id=request.POST['dojo'])
    Ninja.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],dojo=x)
    return redirect('/')
def delete(request,x):
    delx=Dojo.objects.get(id=x)
    delx.delete()
    return redirect('/')