from django.contrib import admin

# Register your models here.
from user_app.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'city', 'image_tag')


admin.site.register(UserProfile,UserProfileAdmin)