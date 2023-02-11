from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CERTIFICATE(models.Model):
    doctor_choices = [
    ('1', 'Doctor_1'),
    ('2', 'Doctor_2'),
    ('3', 'Doctor_3'),
    ('4', 'Doctor_4'),
    ('5', 'Doctor_5'),    
    ]
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    hospitalName = models.CharField(max_length=50)
    user  = models.ForeignKey(User  , on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)
    doctorName = models.CharField(max_length=10 , choices=doctor_choices)

    def __str__(self):
        return self.name










class Doctor(models.Model):
  
    doctorname = models.CharField(max_length=50)
    doctorpassword = models.CharField(max_length=50)

   

    def __str__(self):
        return self.doctorname


