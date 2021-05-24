from django.shortcuts import redirect, render,HttpResponse
from tvshowsapp.models import *

# Create your views here.
def index(request):
    context={
        'x':Show.objects.all()
    }
    return render(request,"index.html",context)
def addshow(request):
    Show.objects.create(title=request.POST['title']
    ,network=request.POST['network'],
    description=request.POST['desc'],
    release_date=request.POST['rdate']
    )
    return redirect('/shows')
def delete(request,id):
    x=Show.objects.get(id=id)
    x.delete()
    return redirect('/shows')
def edit(request,id):
    x=Show.objects.get(id=id)
    context={
        'x':x
    }
    return render(request,"edit.html",context)
def applyedit(request):
    x=Show.objects.get(id=request.POST['id'])
    x.title=request.POST['title']
    x.description=request.POST['desc']
    x.network=request.POST['network']
    if request.POST['rdate']:
        x.release_date=request.POST['rdate']
    x.save()
    return redirect('/shows')
def show(request,id):
    x=Show.objects.get(id=id)
    context={
        'x':x
    }
    return render(request,"show.html",context)