from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages


from Users import models
from Users.forms import registrationForm, fillCustomerForm,fillDeliveryForm,fillRestaurantForm
from django.contrib.auth.models import Group
from Users.models import Customers,Deliverers,PendingRestaurants,Restaurants


def register_customer(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Customers')
            group.user_set.add(user)
            messages.success(request, f"Accout has been created!")
            return redirect('registration-successful')
    else:
        form = registrationForm()
    return render(request, 'Users/registerUser.html', {'form': form})


def register_restaurant(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='RestaurantManager')
            group.user_set.add(user)
            messages.success(request, f"Accout has been created!")
            return redirect('registration-successful')
    else:
        form = registrationForm()
    return render(request, 'Users/registerRestaurant.html', {'form': form})


def register_delivery(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Delivery')
            group.user_set.add(user)
            messages.success(request, f"Accout has been created!")
            return redirect('registration-successful')
    else:
        form = registrationForm()
    return render(request, 'Users/registerDelivery.html', {'form': form})


def registration_successful(request):
    return render(request, 'Users/registrationSuccessful.html')


def register(request):
    return render(request, 'Users/register.html')


def login_redirect(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name == "Customers":
        if Customers.objects.filter(user=request.user).count() == 0:
            return render(request, 'Home/loginRedirect.html')
    elif group.name == "RestaurantManager":
        if Restaurants.objects.filter(user = request.user).count() == 0:
            return render(request,'Home/loginRedirect.html')
    elif group.name == "Delivery":
        if Deliverers.objects.filter(user=request.user).count() == 0:
            return render(request,'Home/loginRedirect.html')
    return redirect('home')



def fill_data(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name == "Customers":
        if Customers.objects.filter(user = request.user).first():
            return redirect('home')
        else:
            return fill_customer(request)
    elif group.name == "RestaurantManager":
        if Restaurants.objects.filter(user = request.user).first():
            return redirect('home')
        else:
            return fill_restaurant(request) 
    elif group.name == "Delivery":
        if Deliverers.objects.filter(user = request.user).first():
            return redirect('home')
        else:
            return fill_delivery(request)
        
    else:
        return redirect('home')


def fill_customer(request):
    if request.method == "POST":
        form = fillCustomerForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            building_number = form.cleaned_data['building_number']
            flat_number = form.cleaned_data['flat_number']
            address = models.Address(city=city, street=street, building_number=building_number, flat_number=flat_number)
            address.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            customer = Customers(user=request.user, first_name=first_name, last_name=last_name, address=address,
                                 phone_number=phone_number)
            customer.save()
            messages.success(request, f"Data have been successfully filled!")
            return redirect('home')
    else:
        form = fillCustomerForm()
    return render(request, 'Users/fillCustomer.html', {'form': form})


def fill_delivery(request):
    if request.method == "POST":
        form = fillDeliveryForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            deliverer = Deliverers(user = request.user,first_name = first_name,last_name = last_name,phone_number = phone_number)
            deliverer.save()
            messages.success(request, f"Data have been successfully filled!")
            return redirect('home')
    else:
        form = fillDeliveryForm(request.POST)
    return render(request,'Users/fillDelivery.html',{'form':form})



def fill_restaurant(request):
    if request.method == "POST":
        form = fillRestaurantForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            building_number = form.cleaned_data['building_number']
            flat_number = form.cleaned_data['flat_number']
            address = models.Address(city=city, street=street, building_number=building_number, flat_number=flat_number)
            address.save()
            restaurant_name = form.cleaned_data['restaurant_name']
            NIP = form.cleaned_data['NIP']
            phone_number = form.cleaned_data['phone_number']
            open_time = form.cleaned_data['open_time']
            close_time = form.cleaned_data['close_time']
            pending_restaurant = PendingRestaurants(user = request.user,address = address,
                                                    restaurant_name = restaurant_name,
                                                NIP = NIP,phone_number = phone_number,
                                                open_time = open_time,close_time = close_time)
            pending_restaurant.save()
            messages.success(request, f"Data have been successfully filled!")
            return redirect('home')
    else:
        form = fillRestaurantForm(request.POST)
    return render(request,'Users/fillRestaurant.html',{'form':form})


    













