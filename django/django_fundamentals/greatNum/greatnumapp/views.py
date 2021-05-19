from django.shortcuts import render ,redirect
import random 	 
# Create your views here.
def index(request):
    request.session['attempts']=0
    request.session['num']=random.randint(1, 10) 
    print(request.session['num'])
    context={
        "count":request.session['num']
    }
    return render(request,"index.html",context)
def check(request):
    request.session['attempts']+=1
    num=int(request.POST['num'])
    if num>request.session['num']:
        request.session['red']=1
    elif num<request.session['num']:
        request.session['red']=1
    else:
        request.session['green']=1
    return render(request,"index.html")
list=[]
def board(request):
    name=request.POST['name']
    attempt=request.session['attempts']
    list.append(
        {'name':name,
        'attempt':attempt}
    )
    context={
        'list':list
    }
    return render(request,"leaderboard.html",context)
def again(request):
    request.session.clear()
    return redirect("/")  # Return the string 'Hello World!' as a response
