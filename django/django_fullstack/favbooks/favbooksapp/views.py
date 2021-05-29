from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from favbooksapp.models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def reg(request):

    if request.POST['password'] == request.POST['confirmpassword']:
        errors=User.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            hashpassword= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            data={'username':request.POST['Username'],
            'password':hashpassword,
            'email':request.POST['email']}
            User.objects.create(username=request.POST['Username'],password=hashpassword,email=request.POST['email'],image=request.FILES['img'])
            request.session['user']=data
            x=User.objects.last()
            request.session['user']['id']=x.id
            return HttpResponse('hello')
def loginz(request):
    psswd=request.POST['password']
    username=request.POST['Username']
    user = User.objects.filter(username=username)
    if user:
        logged_user=user[0]
        
        if bcrypt.checkpw(psswd.encode(), logged_user.password.encode()):

            request.session['user']={
                'username':username,
                'id':logged_user.id,
                'image':logged_user.image.url
            }
            
           
            return redirect('/books')
        else :
            return HttpResponse('password is wrong')
    else:
        return HttpResponse('user is not found')
def logout(request):

    request.session.clear()
    return render(request,"login.html")
def addbook(request):
    title=request.POST['title']
    desc=request.POST['desc']
    user=User.objects.get(id=request.POST['user'])
    Book.objects.create(title=title,desc=desc,uploaded_by=user)
    return redirect('/books')
def books(request):
    books=Book.objects.all()
    user=User.objects.get(id=request.session['user']['id'])
    favbooks=user.liked_books.all().order_by('title')
    context={
        "all":books,
        "favbooks":favbooks,
        "user":user
    }
    return render(request,"books.html",context)
def addtofav(request,id):
    user=User.objects.get(id=request.session['user']['id'])
    book=Book.objects.get(id=id)
    book.users_who_like.add(user)
    
    return redirect('/books')
def viewbook(request,id):
    book=Book.objects.get(id=id)
    user=User.objects.get(id=request.session['user']['id'])
    context={
        'book':book,
        'user':user,
    }
    return render(request,"showbook.html",context)
def unfav(request,id):
    book=Book.objects.get(id=id)
    user=User.objects.get(id=request.session['user']['id'])
    book.users_who_like.remove(user)
    return redirect('/books/'+str(id))
def delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('/books')
def update(request,id):
    book=Book.objects.get(id=id)
    book.title=request.POST['title']
    book.desc=request.POST['desc']
    book.save()
    return redirect('/books/'+str(id))