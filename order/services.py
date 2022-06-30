from .models import Promocode
from django.utils import timezone


def use_promo(promocode, total_price_without_promocode_discount):
    promo_list = Promocode.objects.filter(end_date__gt=timezone.now())
    promocode_discount = 0
    for promo in promo_list:
        if promo.code == promocode:
            promocode_discount = total_price_without_promocode_discount * promo.sale
    return promocode_discount
