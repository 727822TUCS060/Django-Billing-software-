from django.db import models
from Inventory.models import *
# Create your models here.
class Customer(models.Model): #database
    customer_name=models.CharField(max_length =200 , null=True) #default and required
    customer_since=models.CharField(max_length =200 , null=True)
    
    def __str__(self):
        return self.customer_name#to change table name as product name with code as table in admin
class Orders(models.Model): #generate the individual bill for individual product
    customer_reference =models.ForeignKey(Customer , on_delete=models.CASCADE ,null=True) #foreign key is child and refernce is the parent 
    #models.cascade delete the order if the customer is deleted 
    product_reference=models.ForeignKey(Product , on_delete=models.SET_NULL , null=True) #set_null is not delete the customer and product is null
    order_number = models.CharField(max_length=20 ,null=True)
    order_date=models.DateField(null=True)
    quantity=models.IntegerField(default=True)
    amount=models.FloatField(default=0)
    gst_amount=models.FloatField(default=0)
    bill_amount=models.FloatField(default=0) 

    def __str__(self):
        return self.order_number


# Create your models here.
