from django.db import models


class Type(models.Model):
    '''Type of vehicle'''
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    '''Size of vehicle'''
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.l_name} {self.f_name}"


class Vehicle(models.Model):
    vtype = models.ForeignKey('rent.Type', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    real_cost = models.IntegerField()
    vsize = models.ForeignKey('rent.Size', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vtype} - {self.vsize} [created on {self.created}] "


class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField()
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.l_name} {slf.customer.f_name} {self.vehicle.__str__()} {self.rental_date}"


class Rate(models.Model):
    daily_rate = models.FloatField()
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type.name} {self.size.name}"