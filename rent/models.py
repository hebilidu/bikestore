from django.db import models

# Create your models here.

class Type(models.Model):
    '''Type of vehicle'''

class Size(models.Model):
    '''Size of vehicle'''

class Customer(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

class Vehicle(models.Model):
    vtype = models.ForeignKey('rent.Type', on_delete=models.CASCADE)
    # date created
    # real cost (how much it costs)
    vsize = models.ForeignKey('rent.Size', on_delete=models.CASCADE)