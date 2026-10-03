from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login ,logout
from .models import User #import user from the model for signup authentication

#create the manual login form 
def Loginpage(request): 
    if request.user.is_authenticated: #automatic user login
        return redirect('/inventory/products/')
    context ={
        "error": ""
    }
    if request.method == "POST":
        print(request.POST)
        user=authenticate(username = request.POST['username'] , password =request.POST['password']) #name given in the login form 
        if user is not None:
            login(request , user)
            if user.role==0:
                return redirect('/order/customer_table/') #submit login route to next pages
            elif user.role == 1:
                return redirect('/inventory/products_table/')
            elif user.role==2:
                return redirect('/order/orders/')
        else:
            context={
                "error":"Invalid Username or Password"
            }
            return render(request , 'login.html',context)
        
          
    return render(request , 'login.html',context)
def Logout(request):
    logout(request) #it gets the user from login
    return redirect("/")
def signuppage(request):
    context={
        "error":""
    }
    if request.method =="POST":
        user_check=User.objects.filter(username=request.POST['username']) #to check usename is exist or not 
        if len(user_check) > 0:
            context={
                "error":"Username already exist"
            }
            return render(request ,'signup.html',context)

        else:
            new_user=User(username=request.POST['username'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],email=request.POST['email'],age=request.POST['age'],role=request.POST['role']) #left side is model and right side is name given in html
            
            new_user.set_password(request.POST['password']) #to store password as encrypted in database
            
            new_user.save()
            return redirect('/')
        
    return render(request ,'signup.html',context)

# Create your views here.
