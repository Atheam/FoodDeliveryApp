from django.urls import path
from Home import views as Home_views

urlpatterns = [
    path('profile/',Home_views.profile,name='profile'),
    path("changeDelivererStatus/",Home_views.change_deliverer_status,name="changeDelivererStatus"),
    path('', Home_views.home, name='home'),
]