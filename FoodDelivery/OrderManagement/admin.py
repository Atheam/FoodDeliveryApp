from django.contrib import admin
from OrderManagement.models import Menu,Dish,MenuDetails



@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['restaurant']

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name','price','image','description']

@admin.register(MenuDetails)
class DishAdmin(admin.ModelAdmin):
    list_display = ['menu','dish']


