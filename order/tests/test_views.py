from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from authentication.models import CustomUser


class TestOrderView(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email="erzhan@gmail.com", password="erzhan123"
        )
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "erzhan@gmail.com", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        self.url = reverse("order")

    def test_get_queryset_filter(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
