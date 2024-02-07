from django.shortcuts import render, redirect
from .forms import CostumRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import alogout

def register(request):
   if request.method=="POST":
    register_form=CostumRegisterForm(request.POST)
    if register_form.is_valid():
       register_form.save()
       messages.success(request, ("New User Account Created, Login To Get Started!"))
       return redirect('register')
    
   else:  
      register_form=CostumRegisterForm()
      return render(request,'register.html',{'register_form':register_form})
   
   

        

   