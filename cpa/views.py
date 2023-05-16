from django.shortcuts import render,redirect
from . import models
from django.contrib.auth import authenticate
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

# def register(request):
   



def index(request):
    increment=0
    if request.method=='POST':
        increment=increment+1
        # models.Activities.objects.create(nooftimeshared=increment)
        
        increment=increment+1
        Profile.objects.create(user=request.user,sharedfrequency=increment)
        context={"increment":increment}
        return redirect('cpa:index',context)
    else:
        if request.user.is_authenticated:
            return render(request,'cpa/ indexcpa.html')
    
class SignUpView(View):
    def get(self,request,*arg,**kwarg):
        return render(request,'cpa/signup.html')
    def post(self,request):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        # password2=request.POST['password2']
        User.objects.create(first_name=first_name,last_name=last_name,username=username,password=password)
        return redirect('cpa:signin')
    

class SigninView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'cpa/login.html')
    
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        login(request,user)
        return redirect('cpa:index')