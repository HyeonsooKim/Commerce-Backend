from django.db import models
from sorl.thumbnail import ImageField

class Product(models.Model):
    """
    제품 정보 모델
    """
    name = models.CharField(max_length=255)
    image = ImageField(upload_to='photos')
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '{} {}'.format(self.name, self.pub_date)