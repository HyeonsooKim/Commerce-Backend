from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
    """
    제품 데이터 CRUD viewset
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer