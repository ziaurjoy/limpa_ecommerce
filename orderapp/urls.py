

from django.urls import path

from orderapp import views

urlpatterns = [
    path('adding/cart/<int:id>', views.add_to_shoping_cart, name='add-to-shoping-cart'),
    path('shopping/cart', views.card_details, name='shopping-cart'),
    path('cart_delete/<int:id>', views.cart_delete, name='cart-delete'),
]