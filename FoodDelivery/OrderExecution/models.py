from django.db import models
from OrderManagement.models import Dish
from Users.models import Restaurants,Deliverers,Customers
from enum import Enum

class Status(Enum):
    PENDING_RESTAURANT = "PENDING_RESTAURANT"
    PENDING_DELIVERY = "PENDING_DELIVERY"
    INPROGRESS = "INPROGRESS"
    DECLINED = "DECLINED"
    COMPLETED = "COMPLETED"
    


class Order(models.Model):
    price = models.FloatField(default=0)
    status = models.CharField(max_length=16)
    customer = models.ForeignKey(Customers, on_delete= models.CASCADE)
    restaurant = models.ForeignKey(Restaurants, on_delete = models.CASCADE)
    deliverer = models.ForeignKey(Deliverers, on_delete = models.CASCADE, null=True)
    date = models.DateTimeField()


    
class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish,on_delete = models.CASCADE)
    quantity = models.IntegerField()
