from django.shortcuts import render, redirect
from Users.models import Customers, Restaurants, Deliverers
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'Home/home.html')



@login_required()
def profile(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name == "Customers":
        customer = Customers.objects.filter(user = request.user)[0]
        args = {'customer':customer}
        return render(request,'Home/customerProfile.html',args)
    elif group.name == "RestaurantManager":
        restaurant = Restaurants.objects.filter(user = request.user)[0]
        args = {'restaurant':restaurant}
        return render(request,'Home/restaurantProfile.html',args)
    elif group.name == "Delivery":
        deliverer = Deliverers.objects.filter(user = request.user)[0]
        args = {'deliverer':deliverer}
        return render(request,'Home/delivererProfile.html',args)
    else:
        return redirect('home')



