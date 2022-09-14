from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = ImageField(upload_to='photos')
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)
    hit = models.IntegerField(default=0)

    def __str__(self):
        return '{} {}'.format(self.name, self.pub_date)