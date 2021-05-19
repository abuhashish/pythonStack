from django.shortcuts import redirect, render,HttpResponse

# Create your views here.
def register(request):
    return  HttpResponse("placeholder for users to create a new user record")
def login(request):
    return HttpResponse("placeholder for users to log i")
def new(request):
    return redirect("/register")
def users(request):
    return HttpResponse("placeholder to later display all the list of users")