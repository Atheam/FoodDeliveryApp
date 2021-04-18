from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse

from Users import models
from Users.forms import registrationForm, fillCustomerForm
from django.contrib.auth.models import Group
from Users.models import Customers


def registerCustomer(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Customers')
            group.user_set.add(user)
            return redirect('home-successful')
    else:
        form = registrationForm()
    return render(request, 'Users/registerUser.html', {'form': form})


def registerRestaurant(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='RestaurantManager')
            group.user_set.add(user)
            return redirect('login')
    else:
        form = registrationForm()
    return render(request, 'Users/registerRestaurant.html', {'form': form})


def registerDelivery(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Delivery')
            group.user_set.add(user)
            return redirect('login')
    else:
        form = registrationForm()
    return render(request, 'Users/registerDelivery.html', {'form': form})


def registrationSuccessful(request):
    return render(request, 'Users/registrationSuccessful.html')


def register(request):
    return render(request, 'Users/register.html')


def loginRedirect(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name == "Customers":
        if Customers.objects.filter(user=request.user).count() == 0:
            return render(request, 'Home/loginRedirect.html')
    elif group.name == "RestaurantManager":
        pass
    elif group.name == "Delivery":
        pass
    return redirect('home')


def fillData(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name == "Customers":
        return redirect('fillCustomer')
    elif group.name == "RestaurantManager":
        return redirect('fillRestaurant')
    elif group.name == "Delivery":
        return redirect('fillDelivery')
    else:
        return redirect('home')


def fillCustomer(request):
    if request.method == "POST":
        form = fillCustomerForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            building_number = form.cleaned_data['building_number']
            flat_number = form.cleaned_data['flat_number']
            address = models.Address(city=city, street=street, building_number=building_number, flat_number=flat_number)
            address.save()
            first_name = form.cleaned_data['flat_number']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            customer = Customers(user=request.user, first_name=first_name, last_name=last_name, address=address,
                                 phone_number=phone_number)
            customer.save()
            return redirect('home')
    else:
        form = fillCustomerForm()
    return render(request, 'Users/fillCustomer.html', {'form': form})







