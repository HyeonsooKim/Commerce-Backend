from configparser import MAX_INTERPOLATION_DEPTH
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Delivery(models.Model):
    country = models.CharField(max_length=100, verbose_name='국가이름', default='')
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(72)], verbose_name="주문수량")
    cost = models.DecimalField(verbose_name='배송비', max_digits=10, decimal_places=2, default=1200)

class Order(models.Model):
    PAY_STATE = (
        (0, '결제취소'),
        (1, '결제완료'),
        )
    
    DELIVERY_STATE = (
        (0, '배송준비중'),
        (1, '배송중'),
        (2, '배송완료'),
        )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )

    order_date = models.DateTimeField(auto_now_add=True, verbose_name="날짜")
    updated_at = models.DateTimeField(verbose_name='수정 날짜', auto_now=True)
    pay_state = models.PositiveIntegerField(verbose_name='결제 상태', choices=PAY_STATE)
    delivery_state = models.PositiveIntegerField(verbose_name='배송 상태', choices=DELIVERY_STATE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(72)], verbose_name="주문수량")
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10, verbose_name='정가')
    saled_price = models.DecimalField(default=0,  decimal_places=2, max_digits=10, verbose_name='할인금액')
    delivery_cost = models.DecimalField(verbose_name='배송비', max_digits=10, decimal_places=2, default=1200)
    payment_amount = models.DecimalField(verbose_name='최종결제액', default=0, max_digits=10, decimal_places=2)
    buyr_city = models.CharField(max_length=100, verbose_name="도시", default='')
    buyr_country = models.CharField(max_length=100, verbose_name='국가코드', default='')
    buyr_zipx = models.CharField(max_length=30, verbose_name='우편번호', default='')
    vccode = models.IntegerField(verbose_name='국가번호', default=0)
    delivery_num = models.CharField(verbose_name="delivery_num", max_length=20, null=True)

    #모델 인스턴스를 주문 날짜 내림차순 정렬
    class Meta:
        ordering = ('-order_date',)

    def __str__(self):
        return '{} ordered at {}'.format(self.user.username, self.order_date)
