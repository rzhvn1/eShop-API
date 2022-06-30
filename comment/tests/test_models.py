from django.test import TestCase
from ..models import Comment
from authentication.models import CustomUser
from product.models import Product, ProductCategory


class TestCommentModel(TestCase):
    def test_str_method(self):
        author = CustomUser.objects.create_user(
            email="erzhan@gmail.com", password="erzhan123"
        )
        category = ProductCategory.objects.create(name="Laptop")
        product = Product.objects.create(
            title="Macbook", supplier=author, category=category
        )
        comment = Comment.objects.create(
            author=author, content="Good", products=product
        )
        self.assertEqual(
            comment.__str__(), f"Author:{comment.author} Comment:{comment.content}"
        )
