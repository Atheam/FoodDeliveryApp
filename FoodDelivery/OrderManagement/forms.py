from django import forms


class AddDishForm(forms.Form):
    name = forms.CharField()
    price = forms.FloatField()
    description = forms.CharField()
    image = forms.ImageField()