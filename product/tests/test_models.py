from ..models import Product, ProductCategory
from authentication.models import CustomUser
from django.test import TestCase


class TestProductModel(TestCase):
    def test_str_method(self):
        user = CustomUser.objects.create_user(
            email="erzhan@gmail.com", password="erzhan123"
        )
        category = ProductCategory.objects.create(name="Laptop")
        product = Product.objects.create(
            title="Macbook", supplier=user, category=category, price=500
        )
        self.assertEqual(product.__str__(), product.title)


class TestProductCategoryModel(TestCase):
    def test_str_method(self):
        category = ProductCategory.objects.create(name="Laptop")
        self.assertEqual(category.__str__(), category.name)
