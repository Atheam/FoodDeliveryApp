from django.shortcuts import render, redirect
from Users.models import Customers, Restaurants, Deliverers


def home(request):
    return render(request, 'Home/home.html')


