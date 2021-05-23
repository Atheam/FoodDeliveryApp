from django.urls import path
from Users import views as Users_views



urlpatterns = [
    path('registerCustomer/', Users_views.register_customer, name='registerCustomer'),
    path('registerRestaurant/', Users_views.register_restaurant, name='registerRestaurant'),
    path('registerDeliverer/', Users_views.register_delivery, name='registerDeliverer'),
    path('registrationSuccessful/', Users_views.registration_successful, name='registration-successful'),
    path('register/', Users_views.register, name='register'),
    path('fillCustomer/', Users_views.fill_customer, name='fillCustomer'),
    path('loginRedirect/', Users_views.login_redirect, name='loginRedirect'),
    path('fill/', Users_views.fill_data, name='fill'),
    path('fillRestaurant/', Users_views.fill_restaurant, name='fillRestaurant'),
    path('fillDelivery/', Users_views.fill_delivery, name='fillDelivery'),
    
]