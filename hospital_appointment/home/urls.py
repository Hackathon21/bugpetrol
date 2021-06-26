from django import urls
from django.conf.urls import include
from django.urls import path
from home.views import *


urlpatterns = [
     path('',homepage, name = 'homepage'),
     path('home/',homepage, name = 'homepage'),
     path('about/',about, name ='aboutpage'),
     path('login/',login, name ='loginpage'),
]