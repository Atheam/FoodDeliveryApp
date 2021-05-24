from django.contrib import admin
from Users.models import Restaurants,Deliverers,Customers,PendingRestaurants
from OrderManagement.models import Menu
from django.conf import settings
import requests

@admin.register(Deliverers)
class DeliverersAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone_number','latitude','longitude']

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone_number']

@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name','NIP','phone_number','latitude','longitude']
    

@admin.register(PendingRestaurants)
class PendingRestaurantsAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name','NIP','phone_number']
    actions = ['accept_restaurant']

    def accept_restaurant(modeladmin,request,queryset):
        for pending_restaurant in queryset:
            restaurant = Restaurants(user = pending_restaurant.user,restaurant_name = pending_restaurant.restaurant_name,
                                    address = pending_restaurant.address,phone_number = pending_restaurant.phone_number,
                                    NIP = pending_restaurant.NIP,open_time=pending_restaurant.open_time,close_time=pending_restaurant.close_time,)
            
            address= restaurant.address.city + " " + restaurant.address.street + " " + str(restaurant.address.building_number)
            api_response = requests.get('http://www.mapquestapi.com/geocoding/v1/address?key={0}&location={1}'.format(settings.API_KEY,address)).json()
            
            restaurant.latitude = api_response["results"][0]["locations"][0]["latLng"]["lat"]
            restaurant.longitude = api_response["results"][0]["locations"][0]["latLng"]["lng"]
            restaurant.save()
            menu = Menu(restaurant=restaurant)
            menu.save()
            pending_restaurant.delete()







