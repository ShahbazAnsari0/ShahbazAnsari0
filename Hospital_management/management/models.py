from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=20)
    password1=models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Signup(models.Model):
    username = models.CharField(max_length=20)
    password1=models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    bday=models.DateField()
    number=models.IntegerField()
    address=models.CharField(max_length=100)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=40)
    pin_code=models.IntegerField()

    def __str__(self):
        return self.username
