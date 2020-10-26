

from django.urls import path

from orderapp import views

urlpatterns = [
    path('adding/cart/<int:id>', views.add_to_shoping_cart, name='add-to-shoping-cart')
]