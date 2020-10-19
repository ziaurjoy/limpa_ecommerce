
from django.urls import path
from .views import home,single_product
urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>', single_product, name='single-product'),
]