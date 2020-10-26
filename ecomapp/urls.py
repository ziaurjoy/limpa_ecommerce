
from django.urls import path
from .views import home, single_product, filter_of_categories, contact, search_view
urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>', single_product, name='single-product'),
    path('product/<category_name>', filter_of_categories, name='category-name'),
    path('contact', contact, name='contact'),
    path('search_view', search_view, name='search_view'),
]