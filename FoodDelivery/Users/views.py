from django.shortcuts import render
from Users.forms import registrationForm
from django.contrib.auth.models import Group



def registerCustomer(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name = 'Customers')
            group.user_set.add(user)
    else:
        form = registrationForm()
    return render(request,'Users/registerUser.html',{'form':form})

