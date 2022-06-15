
from django.shortcuts import render, HttpResponse ,redirect
from .models import *
def index(request):
    users = Info.objects.all()
    context ={
        'users': users
    }
    return render(request,'index.html',context)


def create(request):
    if request.method == 'POST':
     newUser = Info.objects.create(
        first_name=request.POST['fname'],
         last_name=request.POST['lname'],
         email_address=request.POST['email'],
         age=request.POST['age']
     )
    newUser.save()
    return redirect('/')


