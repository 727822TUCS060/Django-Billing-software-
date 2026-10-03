#from  django.forms import ModelForm 
from django import forms
from .models import *

class Product_form(forms.ModelForm):
    class Meta:
        model =Product #model name
        fields = '__all__' #all fields 
        #fields = ['product_name'] #for specific field
        widgets = {
            'product_name': forms.TextInput(
                attrs={'class':"form-control"} #style and if two or more classes needed include in the same attribute separated by comma 
                ),
            'product_code': forms.TextInput(
                attrs={'class':"form-control"} #style
                            ),
            'price': forms.NumberInput( #number input to have integer as input
                            attrs={'class':"form-control"} #style
                            ),
            'gst': forms.NumberInput(
                            attrs={'class':"form-control"} #style
                            ),
            'picture': forms.FileInput( #field for uploading file and images
                                        attrs={'class':"form-control"} #style
                                        ),
             'file': forms.FileInput( #field for uploading file and images
                                                    attrs={'class':"form-control"} #style
                                                    ),
                        
            

        }
