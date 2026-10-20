
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    product_code = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=0)
    gst = models.IntegerField(default=0)
    food_type = models.BooleanField(default=False)
    picture = models.ImageField(null=True, upload_to='images/')
    file = models.FileField(null=True, upload_to='files/')

    class Meta:
        db_table = 'inventory_product'

    def __str__(self):
        return self.product_name
