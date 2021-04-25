from django import forms




class add_dish_form(forms.Form):
    name = forms.CharField()
    price = forms.FloatField()
    description = forms.CharField()
