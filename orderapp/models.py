from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from product.models import Product


class ShopCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()

    def price(self):
        return self.product.new_price

    def amount(self):
        return self.product.new_price*self.quantity

    def __str__(self):
        return self.product.title