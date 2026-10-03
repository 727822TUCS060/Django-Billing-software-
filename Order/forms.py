from  django.forms import ModelForm 
from .models import *

class Customer_form(ModelForm):
    class Meta:
        model = Customer#model name
        fields = '__all__' #all fields 
        #fields = ['product_name'] #for specific field
class Orders_form(ModelForm):
    class Meta:
        model =Orders #model name
        fields = ['customer_reference' ,'product_reference','order_number','order_date','quantity']