from django import forms

from orderapp.models import ShopCart, Order


class ShopingCartForm(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone', 'address', 'city', 'country', 'transaction_id', 'transaction_image']