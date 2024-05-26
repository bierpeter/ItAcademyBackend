from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class User(models.Model):
    ID_User = models.AutoField(primary_key=True)
    role = models.TextField()
    email = models.TextField()
    password = models.TextField()
    firstName = models.TextField()
    lastName = models.TextField()
    image = models.ImageField(upload_to='user_images/')

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
class Property(models.Model):
    ID_Property = models.AutoField(primary_key=True)
    category = models.TextField()
    image = models.ImageField(upload_to='property_images/')
    conditions = models.BooleanField()
    building = models.TextField()
    floor = models.TextField()
    room = models.TextField()

    def __str__(self):
        return f"{self.category} - {self.building} {self.floor}-{self.room}"


class Employee(models.Model):
    ID_Employee = models.AutoField(primary_key=True)
    category = models.TextField()
    image = models.ImageField(upload_to='employee_images/')
    post = models.TextField()
    firstName = models.TextField()
    lastName = models.TextField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class History(models.Model):
    ID_Epoch = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    ID_Property = models.ForeignKey(Property, on_delete=models.CASCADE)
    ID_Employee = models.IntegerField()

    def __str__(self):
        return f"History record on {self.date}"

class CustomUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    access_level = models.CharField(max_length=10)
    