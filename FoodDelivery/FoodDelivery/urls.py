"""FoodDelivery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from Users import views as Users_views
from Home import views as Home_views
from OrderManagement import views as OrderManagement_views
from OrderExecution import views as OrderExecution_views

urlpatterns = [
    path('', Home_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('registerCustomer/', Users_views.registerCustomer, name='registerCustomer'),
    path('registerRestaurant/', Users_views.registerRestaurant, name='registerRestaurant'),
    path('registerDelivery/', Users_views.registerDelivery, name='registerDelivery'),
    path('registrationSuccessful/', Users_views.registrationSuccessful, name='registration-successful'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    path('register/', Users_views.register, name='register'),
    path('fillCustomer/', Users_views.fillCustomer, name='fillCustomer'),
    path('loginRedirect/', Users_views.loginRedirect, name='loginRedirect'),
    path('fill/', Users_views.fillData, name='fill'),
    path('fillRestaurant/', Users_views.fillRestaurant, name='fillRestaurant'),
    path('fillDelivery/', Users_views.fillDelivery, name='fillDelivery'),
    path('profile/',Home_views.profile,name='profile'),
    path('manageMenu/',OrderManagement_views.manage_menu,name = 'manageMenu'),
    path('addDish/',OrderManagement_views.add_dish,name = 'addDish'),
    path('deleteDish/',OrderManagement_views.delete_dish,name = 'deleteDish'),
    path('browseRestaurants/',OrderManagement_views.browse_restaurants,name = 'browseRestaurants'),
    path('restaurantPage/<int:id>/',OrderManagement_views.restaurant_page,name = 'restaurantPage'),
    path('addToCart/',OrderManagement_views.add_to_cart,name="addToCart"),
    path("cartInfo/",OrderManagement_views.cart_info,name="cartInfo"),
    path("placeOrder/",OrderExecution_views.place_order,name="placeOrder"),
    path("pendingOrders/",OrderExecution_views.pending_orders_r,name="pendingOrders"),
    path('acceptOrderR/',OrderExecution_views.accept_order_r,name ="acceptOrderR"),
    path('acceptOrderD/',OrderExecution_views.accept_order_d,name ="acceptOrderD"),
    path("orderDelivery/",OrderExecution_views.order_delivery,name="orderDelivery"),
    path("changeDelivererStatus/",Home_views.change_deliverer_status,name="changeDelivererStatus"),
    path("completeOrder/",OrderExecution_views.complete_order,name ="completeOrder"),
    path("yourOrder/",OrderExecution_views.your_order,name = "yourOrder"),
    path("declineOrderR/",OrderExecution_views.decline_order_r,name="declineOrderR"),
    path("declineOrderD/",OrderExecution_views.decline_order_d,name = "declineOrderD"),
    path("profile/updateLocation/",OrderExecution_views.update_location,name ="updateLocation"),
    ]
