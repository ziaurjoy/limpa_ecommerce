from django.contrib import admin

# Register your models here.
from product.models import Category,Product,Images

admin.site.register(Category)

admin.site.register(Images)

class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','status','create_at','update_at']
    list_filter = ['title','update_at']
    list_per_page = 10
    search_fields = ['title','new_price','detail']
    inlines = [ProductImagesInline]

admin.site.register(Product,ProductAdmin)