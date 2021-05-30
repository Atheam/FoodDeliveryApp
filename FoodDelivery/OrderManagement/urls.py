from django.urls import path
from OrderManagement import views as OrderManagement_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('manageMenu/',OrderManagement_views.manage_menu,name = 'manageMenu'),
    path('addDish/',OrderManagement_views.add_dish,name = 'addDish'),
    path('deleteDish/',OrderManagement_views.delete_dish,name = 'deleteDish'),
    path('browseRestaurants/',OrderManagement_views.browse_restaurants,name = 'browseRestaurants'),
    path('restaurantPage/<int:id>/',OrderManagement_views.restaurant_page,name = 'restaurantPage'),
    path('addToCart/',OrderManagement_views.add_to_cart,name="addToCart"),
    path("cartInfo/",OrderManagement_views.cart_info,name="cartInfo"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)