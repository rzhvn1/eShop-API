from django.contrib import admin
from .models import Cart, CartItem, Order, Promocode

admin.site.register([Cart, CartItem, Order, Promocode])
