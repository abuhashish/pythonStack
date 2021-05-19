from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    request.session['counter']+=1
    return render(request,"index.html")
def new(request):
    request.session['counter']=0
    return redirect('/')