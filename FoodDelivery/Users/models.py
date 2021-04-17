from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    building_number = models.IntegerField()
    flat_number = models.IntegerField(blank=True)


class Customers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)


class Restaurants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)
    NIP = models.CharField(max_length=12)


class Deliverers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)























