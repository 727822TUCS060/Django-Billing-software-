from django.urls import path
from .views import *#use * for all functions
urlpatterns = [
    #path('products/',products),
    #path('products_table/',AllProducts),
    #path('products_table/delete/<int:id>/',DeleteProducts, name='product_delete'), #id will replace which should be delete
    #path('products_table/update/<int:id>/',ProductUpdate, name='product_update'),
    path('products/',ProductAdd.as_view()),
    path('products_table/',Productlist.as_view()),
    path('products_table/delete/<int:id>/',Productdelete.as_view() , name='product_delete'),
    path('products_table/update/<int:id>/',Productupdate.as_view(),name='product_update'),
]

