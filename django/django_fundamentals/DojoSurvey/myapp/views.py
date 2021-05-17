from django.shortcuts import render, HttpResponse
def index(request):
    return render(request,"index.html")
def show(request):
    context={
    'name':request.POST['name'],
    'location':request.POST['location'],
    'language':request.POST['language'],
    'text':request.POST['text']
    }
    return render(request,"show.html",context)
   