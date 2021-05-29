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
def viewbook(request,id):
    context={
        'book':Book.objects.get(id=id),
        'z':Author.objects.all()
    }
    
    
    return render(request,"view.html",context)
def authors(request):
    context={
        'x':Author.objects.all()
    }
    return render(request,"authors.html",context)
def author(request,id):
    x=Author.objects.get(id=id)
    z=Book.objects.all()
    context={
        'x':x,
        'z':z
    }
    return render(request,"author.html",context)
def addauthor(request):
    Author.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],notes=request.POST['notes'])
    return redirect('/')
def addbookauthor(request,id):
    x=Author.objects.get(id=id)
    i=request.POST['id']
    x.books.add(Book.objects.get(id=i))
    return redirect('/authors/'+str(id))

def addauthorbook(request,id):
    x=Book.objects.get(id=id)
    i=request.POST['id']
    x.authors.add(Author.objects.get(id=i))
    return redirect('/books/'+str(id))