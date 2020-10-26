from django.contrib import admin

# Register your models here.
from ecomapp.models import Setting,ContactMessage

admin.site.register(Setting)
admin.site.register(ContactMessage)