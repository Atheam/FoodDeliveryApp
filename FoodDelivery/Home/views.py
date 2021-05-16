from Users.models import Customers, Restaurants, Deliverers,DelivererStatus
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse



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

def change_deliverer_status(request):
    deliverer = Deliverers.objects.get(user = request.user)
    if deliverer.status == str(DelivererStatus.AVAILABLE):
        deliverer.status = DelivererStatus.NOTAVAILABLE
    else:
        deliverer.status = DelivererStatus.AVAILABLE
    deliverer.save()
    return redirect("profile")







