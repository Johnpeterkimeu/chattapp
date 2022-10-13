from distutils.command.upload import upload
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here
class Location(models.Model):    
     firstname = models.CharField(max_length = 45)
     lastname = models.CharField(max_length = 45)

     age = models.CharField(max_length =3)
     phone_number= models.CharField(max_length =45) 




