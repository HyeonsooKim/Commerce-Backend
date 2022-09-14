from configparser import MAX_INTERPOLATION_DEPTH
from django.db import models
from django.conf import settings
from sorl.thumbnail import ImageField

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )
    order_date = models.DateTimeField()
    pay_state = models.CharField(max_length=20, verbose_name='결제상태')
    quantity = models.IntegerField(default=1, verbose_name="주문수량")
    price = models.PositiveIntegerField(verbose_name='결제금액')
    buyr_city = models.CharField(max_length=100, verbose_name="도시")
    buyr_country = models.CharField(max_length=30, verbose_name='국가코드')
    buyr_zipx = models.CharField(max_length=30, verbose_name='우편번호')
    vccode = models.IntegerField(verbose_name='국가번호')
    # products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product'))

    #모델 인스턴스를 주문 날짜 내림차순 정렬
    class Meta:
        ordering = ('-order_date',)

    # def __str__(self):
    #     return '{} by {}'.format(self.products.name, self.user)
