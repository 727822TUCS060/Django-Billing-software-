from django.db import models

# Create your models here.
class Product(models.Model): #database
    product_name=models.CharField(max_length =200 , null=True) #default and required
    product_code=models.CharField(max_length =200 , null=True)
    price=models.FloatField(default = 0)
    gst=models.IntegerField(default=0)
    food_type=models.BooleanField(default = False)
    picture=models.ImageField(null=True ,upload_to='images/')
    file=models.FileField(null=True ,upload_to='files/')
    def __str__(self):
        return self.product_name #to change table name as product name with code as table in admin