from .models import Order
from rest_framework import serializers
from rest_framework.serializers import ValidationError

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ['id', 'user', 'date', 'quantity',
                            'price', 'sale_price', 'delivery_cost',
                            'payment_amount', 'coupon',
                            'buyr_city', 'buyr_zips', 'vccode']

    def validate(self, data):
        pay_state = data.get('pay_state', None)
        delivery_state = data.get('delivery_state', None)

        if pay_state and pay_state not in (0, 1, 2):
            raise ValidationError("ERROR: 올바르지 않은 결제 상태입니다.")
        elif delivery_state and delivery_state not in (0, 1, 2, 3):
            raise ValidationError("ERROR: 올바르지 않은 배송 상태입니다.")
        return data
    
    def update(self, instance, validated_data):
        """
        주문 내역 수정 함수
        pay_state: 0(결제 취소), 1(결제 대기), 2(결제 완료)
        delivery_state: 0(배송 취소), 1(배송 준비중), 2(배송 중), 3(배송 완료)
        """
        pay_state = validated_data.get('pay_state', instance.pay_state)
        delivery_state = validated_data.get('delivery_state', instance.delivery_state)

        # 결제 취소로 변경하는 경우 쿠폰 사용 초기화
        # if pay_state == 0 and instance.coupon:
        #     coupon = Coupon.objects.get(id=instance.coupon)
        #     coupon.is_used = False
        #     coupon.date = None
        #     coupon.sale_amount = None
        #     coupon.save()

        instance.pay_state = pay_state
        instance.delivery_state = delivery_state
        instance.save()

        return instance