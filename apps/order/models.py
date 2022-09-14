from django.db import models
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )
    order_date = models.DateTimeField(auto_now_add=True)
    pay_state = models.CharField(max_length=20, verbose_name='결제상태', default='')
    quantity = models.IntegerField(default=1, verbose_name="주문수량")
    price = models.PositiveIntegerField(default=0, verbose_name='결제금액')
    buyr_city = models.CharField(max_length=100, verbose_name="도시", default='')
    buyr_country = models.CharField(max_length=30, verbose_name='국가코드', default='')
    buyr_zipx = models.CharField(max_length=30, verbose_name='우편번호', default='')
    vccode = models.IntegerField(verbose_name='국가번호', default=0)
    # products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product'))

    #모델 인스턴스를 주문 날짜 내림차순 정렬
    class Meta:
        ordering = ('-order_date',)

    # def __str__(self):
    #     return '{} by {}'.format(self.products.name, self.user)
