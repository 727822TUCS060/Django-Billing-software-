from django.shortcuts import render ,redirect
from .forms import * #import form data
from .models import *
from django.views import View #to implement class based views
#backend rest use class based views
#function based views 
from django.contrib.auth.mixins import LoginRequiredMixin
"""
def products(request):
    context = {
        'product_form':Product_form #import class from form
    }
    if request.method == "POST":
        product_form=Product_form(request.POST)#shows the data in terminal where entered in ui form and use the context name 
        if product_form.is_valid(): #to check the data request is valid
            product_form.save() #to save the data in the database
    return render(request ,'products.html',context)
def AllProducts(request):
    all_products =Product.objects.all()   #product is model function and objects is data in the model and all is count of data in model
    return render(request, 'products_table.html',{'all_products':all_products}) #use the html file in which the data should show in the ui from the database table 
def DeleteProducts(request,id): #id is the row data
    select_Product=Product.objects.get(id = id)
    select_Product.delete()
    return redirect('/inventory/products_table/')#automatic reload
def ProductUpdate(request ,id):
     select_Product=Product.objects.get(id = id)
     context={
        'product_form':Product_form(instance=select_Product)
     }
     if request.method =='POST':  
        product_form=Product_form(request.POST , instance=select_Product)#instance is for the updation purpose
        if product_form.is_valid(): #to check the data request is valid
            product_form.save() 
            return redirect('/inventory/products_table/')#after updation reload to the product table


     return render(request , 'products.html',context)
"""
class ProductAdd(LoginRequiredMixin,View): #post method
    login_url='/'
    def get(self ,request): # function is constant to send the content from the backend to frontend
        print("class get")
        context = {
                'product_form':Product_form #import class from form
        }
        return render(request ,'products.html',context)
    def post(self , request): #to get from the frontend to backend
        print("class post")
        product_form=Product_form(request.POST , request.FILES)#shows the data in terminal where entered in ui form and use the context name 
        if product_form.is_valid(): #to check the data request is valid
            product_form.save() #to save the data in the database 
            return redirect('/inventory/products_table/')
class Productlist(LoginRequiredMixin,View): #get method
    login_url='/'
    def get(self ,request):
        all_products =Product.objects.all()   #product is model function and objects is data in the model and all is count of data in model
        return render(request, 'products_table.html',{'all_products':all_products})
class Productdelete(LoginRequiredMixin,View):
    login_url='/'
    def get(self ,request , id): #include id for update and delete
        select_Product=Product.objects.get(id = id)
        select_Product.delete()
        return redirect('/inventory/products_table/')
class Productupdate(LoginRequiredMixin,View):
    login_url='/'
    def get(self , request ,id):
        select_Product=Product.objects.get(id = id)
        context={
            'product_form':Product_form(instance=select_Product)
        }
        return render(request , 'products.html' , context)
    def post(self , request ,id):
        select_Product=Product.objects.get(id = id)
        product_form=Product_form(request.POST,instance=select_Product)#shows the data in terminal where entered in ui form and use the context name 
        if product_form.is_valid(): #to check the data request is valid
            product_form.save()
            return redirect('/inventory/products_table/')






# Create your views here.