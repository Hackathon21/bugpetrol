from django import urls
from django.conf.urls import include
from django.urls import path
from home.views import *


urlpatterns = [
     path('',homepage, name = 'homepage'),
]
