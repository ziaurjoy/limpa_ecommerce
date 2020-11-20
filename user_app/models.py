from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(blank=True, max_length=200)
    city = models.CharField(blank=True, max_length=200)
    country = models.CharField(blank=True, max_length=100)
    image = models.ImageField(blank=True, upload_to='user_image')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + '[' + self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src ="{}" heights="50" width="50" />'.format(self.image.url))
    image_tag.short_description = 'Images'

    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return ''
