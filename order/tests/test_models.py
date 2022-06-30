from django.test import TestCase
from authentication.models import CustomUser
from product.models import Product, ProductCategory
from ..models import Cart, CartItem, Order, Promocode
import datetime


class TestCartModel(TestCase):
    def test_str_method(self):
        user = CustomUser.objects.create_user(
            email="erzhan@gmail.com", password="erzhan123"
        )
        cart = Cart.objects.create(user=user)
        self.assertEqual(cart.__str__(), f"Price:{cart.cart_price}")


class TestCartItemModel(TestCase):
    def test_cart_item_price_without_discount_save_successfully(self):
        user = CustomUser.objects.create_user(
            email="erzhan@gmail.com", password="erzhan123"
        )
        cart = Cart.objects.create(user=user)
        category = ProductCategory.objects.create(name="Laptop")
        product = Product.objects.create(
            title="Macbook", supplier=user, category=category, price=500
        )
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity=2)
        self.assertEqual(
            cart_item.cart_item_price_without_discount,
            product.price * cart_item.quantity,
        )


class TestOrderModel(TestCase):
    def test_str_method(self):
        user = CustomUser.objects.create_user(
            email="erzhan@gmail.com", password="erzhan123"
        )
        cart = Cart.objects.create(user=user)
        order = Order.objects.create(cart=cart, user=user)
        self.assertEqual(order.__str__(), f"Total price:{order.total_price}")


class TestPromocodeModel(TestCase):
    def test_str_method(self):
        promocode = Promocode.objects.create(code="1", sale=0.1, end_date="2022-06-25")
        self.assertEqual(promocode.__str__(), f"Code:{promocode.code}")

    def test_is_expired_returns_true_if_end_date_before_now(self):
        now = datetime.datetime.now()
        day_ago = now - datetime.timedelta(days=1)
        promocode = Promocode.objects.create(code="1", sale=0.1, end_date=day_ago)
        self.assertTrue(promocode.is_expired)

    def test_is_expired_returns_false_if_end_date_after_now(self):
        now = datetime.datetime.now()
        day_after = now + datetime.timedelta(days=1)
        promocode = Promocode.objects.create(code="1", sale=0.1, end_date=day_after)
        self.assertFalse(promocode.is_expired)
