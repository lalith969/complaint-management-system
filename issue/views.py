from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from issue.forms import*
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if not User.objects.filter(username=username):
            User.objects.create_user(username=username,email=email,password=password)
            return redirect('/login')
        else:
            messages.error(request,'user already exists')
    return render(request,'signup.html')
@login_required()
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        branch=request.POST['branch']
        issue=request.POST['issue']
        complaint(name=name,branch=branch,issue=issue,status='un solved').save()
        return redirect('home')
    return render(request,'register.html')
@login_required()
def view(request):
    stud=complaint.objects.all()
    return render(request,'view.html',{'st':stud})
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('register')
        else:
            messages.error(request,"Invalid login credentials")
    return render(request,'login.html')
def signout(request):
    logout(request)
    return redirect('home')


    
