from django.db import models
from django.contrib.auth.models import AbstractUser #customizing user models

class User(AbstractUser):
    age=models.IntegerField(default=0)
    role_choices=(
        (0 ,'Admin'),
        (1 ,'Manager'),
        (2 ,'Employee'),
        (3 ,'User'),
    )
    role=models.IntegerField(default=0,choices=role_choices)



# Create your models here.
