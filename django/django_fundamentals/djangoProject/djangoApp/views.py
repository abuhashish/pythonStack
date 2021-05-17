from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("String response from root_method")
def cheetos(request):
    return render(request,"index.html")
def ninja(request,name,age):
    context={
        "htmlname":name,
        "htmlage":age
    }
    return render(request,"index.html",context)