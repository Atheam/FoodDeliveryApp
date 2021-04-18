from django.contrib import admin
from Users.models import Restaurants,Deliverers,Customers,PendingRestaurants

@admin.register(Deliverers)
class DeliverersAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone_number']

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone_number']

@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name','NIP','phone_number']
    

@admin.register(PendingRestaurants)
class PendingRestaurantsAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name','NIP','phone_number']
    actions = ['accept_restaurant']

    def accept_restaurant(modeladmin,request,queryset):
        for pending_restaurant in queryset:
            restaurant = Restaurants(user = pending_restaurant.user,restaurant_name = pending_restaurant.restaurant_name,
                                    address = pending_restaurant.address,phone_number = pending_restaurant.phone_number,
                                    NIP = pending_restaurant.NIP)
            restaurant.save()
            pending_restaurant.delete()







