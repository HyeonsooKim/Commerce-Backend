from rest_framework import viewsets
from .serializers import OrderSerializer
from rest_framework.filters import SearchFilter
from .models import Order

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # 검색기능
    filter_backends = [SearchFilter]
    search_fields = ['user__id']