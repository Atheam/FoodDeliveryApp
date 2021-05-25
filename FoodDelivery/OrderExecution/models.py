from django.db import models
from OrderManagement.models import Dish
from Users.models import Restaurants,Deliverers,Customers
from enum import Enum


class Status(models.TextChoices):
    PENDING_RESTAURANT = "Waiting for restaurant"
    PENDING_DELIVERY = "Waiting for deliverer"
    INPROGRESS = "In progress"
    DECLINED = "Declined"
    COMPLETED = "Completed"
    
class Order(models.Model):
    price = models.FloatField(default=0)
    status = models.CharField(max_length=50,choices = Status.choices)
    customer = models.ForeignKey(Customers, on_delete= models.CASCADE)
    restaurant = models.ForeignKey(Restaurants, on_delete = models.CASCADE)
    deliverer = models.ForeignKey(Deliverers, on_delete = models.CASCADE, null=True)
    restaurant_rating = models.IntegerField(default = 0)
    deliverer_rating = models.IntegerField(default = 0)
    date = models.DateTimeField()

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish,on_delete = models.CASCADE)
    quantity = models.IntegerField()



