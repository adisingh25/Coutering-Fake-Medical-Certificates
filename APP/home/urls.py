from django.contrib import admin
from django.urls import path
from django.shortcuts import render,HttpResponse,redirect
from .views import home,doctor,patient,signup,applyCertificate,signout,acceptApplication,change_status,download

urlpatterns = [ 
   path('', home, name='home'),
   path('doctor/', doctor, name='doctor'),
   path('patient/', patient, name='patient'),
   path('signup/', signup),
   path('apply/',applyCertificate,name='applyCertificate'),
   path('acceptApplication/', acceptApplication, name='acceptApplication'),
   path('change-status/<int:id>', change_status),
   path('download/',download),
   path('logout/', signout),
]