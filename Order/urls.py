from django.urls import path
from .views import * #use * for all functions
urlpatterns =[
    path('customers/',Customers),
    path('customer_table/',AllCustomers),
    path('customer_table/delete/<int:id>/',DeleteCustomers, name='customer_delete'), #id will replace which should be delete
    path('customer_table/update/<int:id>/',CustomerUpdate, name='customer_update'),
    path('add/orders/',OrdersAdd),
    path('orders/',OrderList),
    path('delete/order/<int:id>/',OrdersDelete , name='Order_delete'),
    path('update/order/<int:id>/',OrderUpdate , name='Order_update'),


]
