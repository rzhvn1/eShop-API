from django.contrib import admin
from .models import CustomUser, Card

admin.site.register([CustomUser, Card])
