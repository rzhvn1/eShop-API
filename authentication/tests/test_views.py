from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from ..models import CustomUser


class TestCardModelViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        CustomUser.objects.create_user(email="erzhan@gmail.com", password="erzhan123")
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "erzhan@gmail.com", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        self.url = reverse("card-list")

    def test_perform_create_request_user(self):
        data = {
            "number": 123456,
            "holder_name": "Erzhan M",
            "date": "2024-06-23",
            "code": 123,
            "balance": 10000,
        }
        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class TestUpdatePassword(APITestCase):
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

    def test_wrong_old_password(self):
        data = {"old_password": "wrong", "new_password": "admin123456"}
        self.response = self.client.put(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_serializer_is_not_valid(self):
        data = {}
        self.response = self.client.put(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
