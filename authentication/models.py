from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    first_name = models.CharField(max_length=255, verbose_name="first_name")
    last_name = models.CharField(max_length=255, verbose_name="last_name")
    address = models.CharField(
        max_length=255, verbose_name="address", null=True, blank=True
    )
    phone = models.CharField(
        max_length=255, verbose_name="phone", null=True, blank=True
    )

    def __str__(self):
        return self.email


class Card(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="cards")
    number = models.PositiveIntegerField(default=0)
    holder_name = models.CharField(max_length=50, default="Full Name")
    date = models.DateField()
    code = models.IntegerField(default=0)
    balance = models.FloatField(default=0)
    status = models.CharField(
        choices=(
            ("default", "default"),
            ("non active", "non active"),
        ),
        max_length=15,
        default="non active",
    )
