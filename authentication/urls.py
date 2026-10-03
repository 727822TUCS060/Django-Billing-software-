from django.urls import path
from .views import *
urlpatterns=[
    path('' ,Loginpage), #'' defines landing page of website as first page
    path('logout/',Logout),
    path('signup/',signuppage)
]