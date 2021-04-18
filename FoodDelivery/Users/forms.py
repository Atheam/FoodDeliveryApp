from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class registrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class fillCustomerForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    city = forms.CharField()
    street = forms.CharField()
    building_number = forms.IntegerField()
    flat_number = forms.IntegerField()
    phone_number = forms.CharField()




