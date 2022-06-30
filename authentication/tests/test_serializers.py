from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from ..models import CustomUser


class TestCustomUserRegisterSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("register-list")
        CustomUser.objects.create_user(email="erzhan@gmail.com", password="erzhan123")

    def test_user_create_successfully(self):
        data = {
            "first_name": "Erzhan",
            "last_name": "Muratov",
            "email": "erzhan1@gmail.com",
            "password": "erzhan123",
            "check_password": "erzhan123",
            "address": "Neobis",
            "phone": "+123456789",
            "cards": [
                {
                    "number": 123456,
                    "holder_name": "Erzhan M",
                    "date": "2024-06-23",
                    "code": 123,
                    "balance": 10000,
                }
            ],
        }
        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_if_passwords_does_not_match(self):
        data = {
            "first_name": "Erzhan",
            "last_name": "Muratov",
            "email": "erzhan1@gmail.com",
            "password": "erzhan123",
            "check_password": "erzhan123456",
            "address": "Neobis",
            "phone": "+123456789",
            "cards": [
                {
                    "number": 123456,
                    "holder_name": "Erzhan M",
                    "date": "2024-06-23",
                    "code": 123,
                    "balance": 10000,
                }
            ],
        }
        self.response = self.client.post(self.url, data, format="json")
        self.assertContains(
            self.response, text="Passwords doesnt match!", status_code=400
        )


class TestChangePasswordSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        CustomUser.objects.create_user(email="erzhan@gmail.com", password="erzhan123")
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "erzhan@gmail.com", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        self.url = reverse("change-password")

    def test_password_changed_successfully(self):
        data = {"old_password": "erzhan123", "new_password": "admin123456"}
        self.response = self.client.put(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)


class TestLogoutSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        CustomUser.objects.create_user(email="erzhan@gmail.com", password="erzhan123")
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "erzhan@gmail.com", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        self.url = reverse("auth_logout")

    def test_logout_successfully(self):
        refresh_token = self.res.data["refresh"]
        data = {"refresh": refresh_token}
        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_logout_invalid_token(self):
        data = {"refresh": "1"}
        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
