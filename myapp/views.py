from ast import Is
#from curses import ACS_GEQUAL

import email
from enum import auto
from imaplib import _Authenticator
import imp
from operator import index
#from tkinter import Widget
#from tkinter.tix import Form
from urllib import request, response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import is_valid_path
from account.models import Account
from myapp.models import  Location
import myapp
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password

# Create your views here.


def home(request):
    return render(request,"home.html")
def Login(request):

  if request.method =='POST':

      username= request.POST.get('username')
      Password= request.POST.get("Password")

      user = authenticate(request, username=username,password=Password)
      if user  != None:
          login(request, user)          
          return redirect('chat')
  
      return HttpResponse('wrong password or username')       
 
    
  return render(request,"loginpage.html")
    
def save_data(request):
   if request.method == 'POST':
      firstname= request.POST.get('firstname')
      lastname= request.POST.get("lastname")
      age= request.POST.get("age")
      phone_number= request.POST.get("phone_number")

      
      Location.objects.create( firstname=firstname,
       lastname= lastname, age= age,
       phone_number=phone_number)

      return redirect('home')   

def sign_up(request):
   if request.method == 'POST':
    form= index(request.POST),
    if form.is_valid():
      user= form.save
      user.refresh_from_db
      user.save()
      raw_password = form.cleaned_data.get('password1')
      user= _Authenticator(username= user.username, password=raw_password)
      Login(request,user)
      return redirect('home')

   else:
      #form=loginpage()
      return(render,request,'home.html',{'form':form})

def register(request):
    if request.method == 'POST':
          username= request.POST.get('username')
          first_name= request.POST.get('first_name')
          last_name=request.POST.get('last_name')
          email=request.POST.get('email')
          Password=request.POST.get("Password")
          repeat=request.POST.get("repeat")
          age= request.POST.get("age")
          phone_number= request.POST.get("phone_number")
          photo= request.FILES.get("photo")

          if Password == repeat:  
            Password=make_password(Password)                
      
            Account.objects.create(username = username,
            password= Password,first_name=first_name,last_name= last_name,age=age,phone_number=phone_number,photo=photo,email=email)

            return redirect('Login')  
    
        

          return HttpResponse('Password does not match ')  
    
    return render(request,'register.html')



def chat(request):
        return render(request,"chattpage.html")
       


def profile(request):
    user_data={}
    if request.user.is_authenticated:
      print("te user is authenticates")
      user=request.user
      print("the username is",user.username, user.email, user.phone_number)
      first_name=user.first_name
      last_name= user.last_name
      username=user.username
      age=user.age
      phone_number=user.phone_number
      photo=user.photo
      email=user.email
     

      user_data['first_name'] = first_name
      user_data['last_name'] = last_name
      user_data['username'] = username
      user_data['age'] = age
      user_data['phone_number']= phone_number
      user_data['email'] = email
      user_data['photo'] = photo
      
    else:  
      print("the user not authenticated") 
      

    return render(request,'chattpage.html',user_data)

      
def  dev(request):
     return render(request,"dev.html")


