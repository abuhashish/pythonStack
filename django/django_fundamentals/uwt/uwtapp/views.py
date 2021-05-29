from django.shortcuts import redirect, render,HttpResponse
from .models import users
# Create your views here.
def index(request):
    context={
        'x':users.objects.all()
    }
    return render(request,"index.html",context)
def add(request):
    # conext={
    #     'fname':request.POST['fname'],
    #     'lname':request.POST['lname'],
    #     'email':request.POST['email'],
    #     'age':request.POST['age']
    # }
    users.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email_address=request.POST['email'],age=int(request.POST['age']))
    return redirect("/")
def get(request,id):
    context={
        'fname':users.objects.get(id=id).first_name,
        'lname':users.objects.get(id=id).last_name,
        'email':users.objects.get(id=id).email_address,
        'age':users.objects.get(id=id).age,
    }
    return render(request,"get.html",context)
def delete(request,id):
    x=users.objects.get(id=id)
    x.delete()
    
    return redirect ("/")
def update(request,id):
    context={
        'fname':users.objects.get(id=id).first_name,
        'lname':users.objects.get(id=id).last_name,
        'email':users.objects.get(id=id).email_address,
        'age':users.objects.get(id=id).age,
    }
    return render(request,"update.html",context)