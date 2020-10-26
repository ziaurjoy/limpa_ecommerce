from django.contrib import admin
from orderapp.models import ShopCart
# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'price', 'amount']

admin.site.register(ShopCart,ShopCartAdmin)