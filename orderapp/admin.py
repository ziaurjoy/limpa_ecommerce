from django.contrib import admin
from orderapp.models import ShopCart, Order, OderProduct
# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'price', 'amount']

class OrderProductline(admin.TabularInline):
    model = OderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'total', 'status', 'transaction_id']
    list_filter = ['status']
    # readonly_fields = ('user', 'full_name', 'phone', 'address', 'city', 'country', 'total', 'ip', 'transaction_id', 'image_tag')
    can_delete = False
    inlines = [OrderProductline]

class OderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']



admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OderProduct, OderProductAdmin)