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