from rest_framework import viewsets, mixins
from .serializers import OrderSerializer, OrderTestSerializer
from rest_framework.filters import SearchFilter
from .models import Order, Order
import time

class OrderViewSet(viewsets.ModelViewSet):
    """
    주문 내역 조회(리스트, 검색), 수정 Viewset
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # 검색기능(유저 이름으로 검색)
    filter_backends = [SearchFilter]
    search_fields = ['user__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        특정 날짜 또는 날짜 범위에 따른 필터링
        결제 상태 또는 배송 상태에 따른 필터링
        query_params : date, start_date, end_date, pay_state, delivery_state
        """
        queryset = self.queryset
        params = self.request.query_params
        if params.get('date'):
            queryset = queryset.filter(order_date__date=params.get('date'))

        if params.get('start_date'):
            queryset = queryset.filter(order_date__gte=params.get('start_date'))

        if params.get('end_date'):
            queryset = queryset.filter(order_date__lte=params.get('end_date'))

        if params.get('pay_state'):
            queryset = queryset.filter(pay_state=params.get('pay_state'))

        if params.get('delivery_state'):
            queryset = queryset.filter(delivery_state=params.get('delivery_state'))

        return queryset

class OrderTestViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderTestSerializer