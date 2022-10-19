from distutils.command.upload import upload
from email.policy import default
from enum import unique
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import AbstractUser



# Create your models here
class Location(models.Model):    
     firstname = models.CharField(max_length = 45)
     lastname = models.CharField(max_length = 45)

     age = models.CharField(max_length =5, default="")
     phone_number= models.CharField(max_length =10, default="") 


 
 


