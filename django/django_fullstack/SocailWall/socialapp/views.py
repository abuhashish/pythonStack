from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from socialapp.models import *
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
            return redirect('/welcome')
def welcome(request):
    if 'user' in request.session:
        context={
            'x':User.objects.last(),
            'y':Message.objects.all()
        }
        return render(request,'welcome.html',context)
    return redirect('/login')
def logout(request):

    request.session.clear()
    return render(request,"login.html")
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
            }
           
            return redirect('/welcome')
        else :
            return HttpResponse('password is wrong')
    else:
        return HttpResponse('user is not found')
def addmessage(request):
    message=request.POST['message']
    user=User.objects.get(id=request.session['user']['id'])
    Message.objects.create(message=message,user=user)
    return redirect('/welcome')
def addcomment(request,id):
    messageid=Message.objects.get(id=id)
    userid=User.objects.get(id=request.session['user']['id'])
    comment=request.POST['text']
    Comment.objects.create(user=userid,message=messageid,comment=comment)
    return redirect('/welcome')