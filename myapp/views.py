from ast import Is
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
from myapp.models import Location
import myapp
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request,"home.html")
def Login(request):

  if request.method =='POST':

      username= request.POST.get('username')
      Password= request.POST.get("Password")

      user_entry= User.objects.get(username=username)
      if user_entry:
        password = user_entry.password
        if Password == password:
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
          Password= request.POST.get("Password")
          repeat= request.POST.get("repeat")

          if Password == repeat:                  
      
            User.objects.create( username= username,
            password= Password)

            return redirect('Login')   

          return HttpResponse('Password does not match ')  
    return render(request,'register.html')


def chat(request):
        return render(request,"chattpage.html")



def messae(request):
 if request.method == 'POST':
   firstname= request.post.get('firstname')
   lastname = request.post.get('lastname')
   age= request.post.get('age')
   phone_number= request.post.get('phone_number')

user_entry= User.objects.get()
if user_entry:
      firstname = user_entry.firstname
      firstname== firstname
      lastname = user_entry.lastname
      lastname==lastname
      age= user_entry.age
      age==age
      phone_number= user_entry.phone_number
      phone_number==phone_number

   

      
      
      

        
  