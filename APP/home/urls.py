
from django.contrib import admin
from django.urls import path
from django.shortcuts import render,HttpResponse,redirect
from home.views import home,doctor,patient,signup,applyCertificate,signout






urlpatterns = [ 
   path('', home, name='home'),
   path('doctor/', doctor, name='doctor'),
   path('patient/', patient, name='patient'),
   path('signup/', signup),
   path('apply/', applyCertificate, name='applyCertificate'),
   path('logout/', signout),
]