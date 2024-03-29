# django rest api
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser
# local modules
from .models import Coupon, CouponType
from .serializers import CouponSerializer, CouponTypeSerializer, CouponStatisticsSerializer
from .permissions import IsAdminOrCreateReadOnly


class CouponTypeViewSet(viewsets.ModelViewSet):
    """ 쿠폰 타입 CRUD Viewset """
    queryset = CouponType.objects.all()
    serializer_class = CouponTypeSerializer
    # 테스트를 위해 permission 주석 처리
    # permission_classes = [IsAdminUser]


class CouponViewSet(viewsets.ModelViewSet):
    """ 쿠폰 CRUD Viewset """
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    # 테스트를 위해 permission 주석 처리
    # permission_classes = [IsAdminOrCreateOnly]


class CouponStatisticsViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    """ 쿠폰 타입별 사용 내역 통계 Viewset """
    queryset = CouponType.objects.all()
    serializer_class = CouponStatisticsSerializer