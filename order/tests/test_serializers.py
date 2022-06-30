from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from authentication.models import CustomUser
from ..models import Cart, CartItem, Promocode, Order
from product.models import Product, ProductCategory


class TestCartSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email="erzhan@gmail.com", password="erzhan123"
        )
        Promocode.objects.create(code="1", sale=0.1, end_date="2022-06-26")
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "erzhan@gmail.com", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        self.url = reverse("cart")

    def test_get_cart_price_method_without_product_discount(self):
        category = ProductCategory.objects.create(name="Laptop")
        product = Product.objects.create(
            title="Macbook", supplier=self.user, category=category, price=500
        )
        cart_data = {"promocode": "1"}
        self.cart = self.client.post(self.url, cart_data, format="json")
        cart_item_data = {
            "product": product.id,
            "cart": self.cart.data["id"],
            "quantity": 2,
        }
        url = reverse("cart-item")
        self.cart_item = self.client.post(url, cart_item_data, format="json")
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_get_cart_price_method_with_product_discount(self):
        category = ProductCategory.objects.create(name="Laptop")
        product = Product.objects.create(
            title="Macbook",
            supplier=self.user,
            category=category,
            price=500,
            discount=0.1,
        )
        cart_data = {"promocode": "1"}
        self.cart = self.client.post(self.url, cart_data, format="json")
        cart_item_data = {
            "product": product.id,
            "cart": self.cart.data["id"],
            "quantity": 2,
        }
        url = reverse("cart-item")
        self.cart_item = self.client.post(url, cart_item_data, format="json")
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)


class TestOrderSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email="erzhan@gmail.com", password="erzhan123"
        )
        Promocode.objects.create(code="1", sale=0.1, end_date="2022-06-26")
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "erzhan@gmail.com", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        category = ProductCategory.objects.create(name="Laptop")
        product = Product.objects.create(
            title="Macbook",
            supplier=self.user,
            category=category,
            price=500,
            discount=0.1,
        )
        self.cart = Cart.objects.create(user=self.user, promocode="1")
        self.cart_item = CartItem.objects.create(
            product=product, cart=self.cart, quantity=1
        )
        self.cart_res = self.client.get(reverse("cart-detail", args=[self.cart.id]))
        self.order = Order.objects.create(user=self.user, cart=self.cart)

    def test_get_total_price_method(self):
        self.url = reverse("order-detail", args=[self.order.id])
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
