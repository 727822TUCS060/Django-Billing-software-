from django.shortcuts import render , redirect
from .forms import * #import form data
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def Customers(request):
    context = {
        'customer_form':Customer_form #import class from form
    }
    if request.method == "POST":
        customer_form=Customer_form(request.POST)#shows the data in terminal where entered in ui form and use the context name 
        if customer_form.is_valid(): #to check the data request is valid
            customer_form.save() #to save the data in the database
            return redirect('/order/customer_table/')
    return render(request ,'customer.html',context)
@login_required(login_url='/')    
def AllCustomers(request):
    print("Authenticated:", request.user.is_authenticated) # authentication sattus and user name 
    print("User:", request.user)
    all_customers =Customer.objects.all()   #product is model function and objects is data in the model and all is count of data in model
    return render(request, 'customer_table.html',{'all_customers':all_customers}) #use the html file in which the data should show in the ui from the database table 
@login_required(login_url='/')
def DeleteCustomers(request,id): #id is the row data
    select_Customer=Customer.objects.get(id = id)
    select_Customer.delete()
    return redirect('/order/customer_table/')#automatic reload
@login_required(login_url='/')
def CustomerUpdate(request ,id):
     select_Customer=Customer.objects.get(id = id)
     context={
        'customer_form':Customer_form(instance=select_Customer)
     }
     if request.method =='POST':  
        customer_form=Customer_form(request.POST , instance=select_Customer)#instance is for the updation purpose
        if customer_form.is_valid(): #to check the data request is valid
            customer_form.save() 
            return redirect('/order/customer_table/')#after updation reload to the product table


     return render(request , 'customer.html',context)
@login_required(login_url='/')
def OrdersAdd(request):
    context={
        'order_form':Orders_form()

    }
    if request.method == 'POST':
        selected_product =Product.objects.get(id =request.POST['product_reference'])
        amount=float(selected_product.price) * float(request.POST['quantity'])
        gst_amount =(amount*selected_product.gst)/100
        bill_amount = amount + gst_amount
        new_order =Orders(customer_reference_id =request.POST['customer_reference'],product_reference_id=request.POST['product_reference'],order_number=request.POST['order_number'],order_date=request.POST['order_date'],quantity =request.POST['quantity'], amount=amount , gst_amount=gst_amount , bill_amount=bill_amount ) 
        new_order.save()
        return redirect('/order/orders/')
    return render(request , 'orders_add.html' ,context) 
@login_required(login_url='/')
def OrderList(request):
    context ={
        'all_orders':Orders.objects.all()
    }
    return render(request , 'orders.html' , context)
@login_required(login_url='/')
def OrdersDelete(request ,id):
    order=Orders.objects.get(id =id)
    order.delete()
    return redirect('/order/orders/')
@login_required(login_url='/')
def OrderUpdate(request ,id):
    select_Order=Orders.objects.get(id = id)
    context={
        'order_form':Orders_form(instance=select_Order)
     }
    if request.method == 'POST':
        selected_product =Product.objects.get(id =request.POST['product_reference'])
        amount=float(selected_product.price) * float(request.POST['quantity'])
        gst_amount =(amount*selected_product.gst)/100
        bill_amount = amount + gst_amount
        order_filter=Orders.objects.filter(id=id)
        order_filter.update(customer_reference_id =request.POST['customer_reference'],product_reference_id=request.POST['product_reference'],order_number=request.POST['order_number'],order_date=request.POST['order_date'],quantity =request.POST['quantity'], amount=amount , gst_amount=gst_amount , bill_amount=bill_amount )
        
        
        return redirect('/order/orders/')
   #after updation reload to the product table


    return render(request , 'orders_add.html',context)

# Create your views here.
