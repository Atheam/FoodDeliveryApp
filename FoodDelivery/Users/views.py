from django.shortcuts import render, redirect
from Users.forms import registrationForm
from django.contrib.auth.models import Group


def registerCustomer(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Customers')
            group.user_set.add(user)
            return redirect('registration-successful')
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
            return redirect('registration-successful')
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
            return redirect('registration-successful')
    else:
        form = registrationForm()
    return render(request, 'Users/registerDelivery.html', {'form': form})


def registrationSuccessful(request):
    return render(request, 'Users/registrationSuccessful.html')