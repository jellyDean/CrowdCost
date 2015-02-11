__author__ = 'Sam'
from django import forms


class UserInput(forms.Form):
    category = forms.ChoiceField(widget = forms.Select(),
                 choices = ([('CABLE','CABLE'),('PHONE','PHONE'),('WEDDINGS','WEDDINGS')]),
                 initial='3', required = True)
    provider = forms.ChoiceField(widget = forms.Select(),
                 choices = ([('TWC','TWC'),('VERIZON','VERIZON'),('WEDDINGS','WEDDINGS')]),
                 initial='3', required = True)
    name = forms.CharField(max_length=100)
    zipcode = forms.CharField(max_length=100)
    price = forms.CharField(max_length=100)

