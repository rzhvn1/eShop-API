from rest_framework import viewsets, permissions
from .models import ProductCategory, Product
from .serializers import ProductCategorySerializer, ProductSerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class ProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]
