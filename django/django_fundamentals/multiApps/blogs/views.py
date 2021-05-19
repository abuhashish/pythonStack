from django.shortcuts import redirect, render,HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(response):
    return redirect('/')
def show(response):
    return HttpResponse("placeholder to display blog number: {{number}}")
def edit(response):
    return HttpResponse("placeholder to edit blog {{number}}")
def destroy(response):
    return redirect("/")