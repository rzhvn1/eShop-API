from django.test import TestCase
from ..models import CustomUser


class TestCustomUserModel(TestCase):
    def test_str_method(self):
        user = CustomUser.objects.create_user(
            email="erzhan@gmail.com", password="erzhan123"
        )
        self.assertEqual(user.__str__(), user.email)
