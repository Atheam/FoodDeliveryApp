from django.db import models
from django.contrib.auth.models import User
from OrderManagement.models import Menu
from django.utils import timezone
from enum import Enum


class DelivererStatus(Enum):
    NOTAVAILABLE = "NOTAVAILABLE"
    AVAILABLE = "AVAILABLE"
    BUSY = "BUSY"

    

class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    building_number = models.IntegerField()
    flat_number = models.IntegerField(blank=True)

class Customers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)

class Restaurants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)
    NIP = models.CharField(max_length=12)
    open_time = models.TimeField()
    close_time = models.TimeField()
    latitude = models.CharField(max_length= 100,default = "0.0")
    longitude = models.CharField(max_length = 100, default = "0.0")
    
class PendingRestaurants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)
    NIP = models.CharField(max_length=12)
    open_time = models.TimeField()
    close_time = models.TimeField()

class Deliverers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length= 16,default= DelivererStatus.NOTAVAILABLE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=9)
    latitude = models.CharField(max_length= 100,default = "0.0")
    longitude = models.CharField(max_length = 100, default = "0.0")



























