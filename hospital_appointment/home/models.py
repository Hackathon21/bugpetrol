from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField
from django.http.request import validate_host

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length= 30)
    email = models.EmailField(unique=True)
    gender = models.CharField( max_length=50)
    phone = models.CharField( max_length=50)
    age = models.CharField(max_length=50)
    bloodgroup = models.CharField(max_length=50)
    address = models.CharField( max_length=150)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length= 30)
    email = models.EmailField(unique=True)
    gender = models.CharField( max_length=50)
    phone = models.CharField( max_length=50)
    age = models.CharField(max_length=50)
    bloodgroup = models.CharField(max_length=50)
    address = models.CharField( max_length=150)
    speciality = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class appointment(models.Model):
    doctorname = models.CharField( max_length=50)
    patientname = models.CharField( max_length=50)
    doctoremail = models.EmailField( max_length=254)
    patientemail =models.EmailField( max_length=254)
    appointmentdate = models.DateField()
    appointmenttime = models.TimeField()
    symptoms = models.TextField()
    prescriptiom = models.TextField()
    status =models.BooleanField()
    
    def __str__(self):
        return self.patientname ,"you have appointmnet with",self.doctorname ,"on", self.appointmentdate

    