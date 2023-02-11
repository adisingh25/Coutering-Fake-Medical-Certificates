from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# from datetimewidget.widgets import DateTimeWidget

# Create your models here.
class CERTIFICATE(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    hospitalName = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)
    doctorName = models.CharField(max_length=10)
    ticketid=models.IntegerField(unique=True)
    isverified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Doctor(models.Model):
  
    doctorname = models.CharField(max_length=50)
    doctorpassword = models.CharField(max_length=50)
    hospitalname=models.CharField(max_length=50,default="HospitalA")

    def __str__(self):
        return self.doctorname

class certificateissue(models.Model):
    datetime=models.DateField(auto_now_add=True)
    slipno=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    docname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    bloodgp=models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    problem = models.CharField(max_length=200)
    nextvisitafter = models.CharField(max_length=200)
    HospitalName=models.CharField(max_length=200)


    def __str__(self):
        return self.name