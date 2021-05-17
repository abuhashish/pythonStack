from django.http.response import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
i=0
def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse("placeHolder")
def new(request):
    return render(request,"form.html")
def create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        context={
            "num":i,
            "title":title,
            "content":content
        }
    i+=1
    
    
    return redirect("/")
def show(request,num):
    print(num)
    context={
        'num' : num
    }
    return render(request,"show.html",context)
def edit(request,num):
    return redirect('/')
def delete(request,num):
    return redirect('/')