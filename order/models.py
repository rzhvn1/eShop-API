from django.db import models
from authentication.models import CustomUser
from product.models import Product
from datetime import datetime


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cart_price = models.FloatField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    promocode = models.CharField(max_length=10, blank=True, null=True, default="1")

    def __str__(self):
        return f"Price:{self.cart_price}"


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart")
    quantity = models.PositiveIntegerField(default=1)
    cart_item_price_without_discount = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.cart_item_price_without_discount = self.quantity * self.product.price
        super().save(*args, **kwargs)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Total price:{self.total_price}"


class Promocode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    sale = models.FloatField(default=0.1)
    end_date = models.DateField()

    @property
    def is_expired(self):
        if datetime.now() > self.end_date:
            return True
        return False

    def __str__(self):
        return f"Code:{self.code}"
