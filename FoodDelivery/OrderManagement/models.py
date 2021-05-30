from django.db import models




class Menu(models.Model):
    restaurant = models.ForeignKey("Users.Restaurants", on_delete = models.CASCADE)
    

class Dish(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length = 500)
    image = models.ImageField(upload_to='images/')

    
class MenuDetails(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete = models.CASCADE)



