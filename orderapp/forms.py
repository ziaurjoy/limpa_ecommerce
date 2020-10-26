from django import forms

from orderapp.models import ShopCart



class ShopingCartForm(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']