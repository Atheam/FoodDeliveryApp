from django.contrib import admin

from OrderExecution.models import Order,OrderDetails

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['restaurant','price','date','status','deliverer']

@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['order','dish','quantity']





