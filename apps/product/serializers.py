from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """
    제품 시리얼라이저
    """
    class Meta:
        model = Product
        fields = "__all__"