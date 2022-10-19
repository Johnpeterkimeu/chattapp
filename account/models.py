
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None): #can add others eg fname,lname etc if required
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email), #email tolowercase
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user




class Account(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    age= models.CharField(max_length=5, default="")
    phone_number=models.CharField(max_length=10)
    photo= models.ImageField(upload_to ='images')

    #required fields when creating custom user
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'   #login field
    REQUIRED_FIELDS = ['username'] #required during registering

    objects = MyAccountManager()  #pointing to the manager

    def __str__(self):
        # return self.email
        return self.email

    #required functions for custom user
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin #do stuffs if admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
