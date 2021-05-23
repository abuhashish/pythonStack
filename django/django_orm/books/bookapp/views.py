from django.shortcuts import redirect, render,HttpResponse
from bookapp.models import *
# Create your views here.
def index(request):
    context={
        'x':Book.objects.all()
            }
    return render(request,"index.html",context)
def addbook(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect('/')