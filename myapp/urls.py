from django. urls import path
from myapp import views
import myapp
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [

path('',views.home, name='home'),
path('chat/',views.profile, name='chat'),
path("auth/login", views.Login, name="Login"),
path("save_data",views.save_data,name='save_data'),
path("home/",views.sign_up,name="signup"),
path("register/",views.register,name="register"),
 #path("redirect/",views.redirect,name="redirect")
 path('',views.dev, name='dev')
]