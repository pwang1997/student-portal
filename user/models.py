from django.db import models
from django.forms import PasswordInput

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length = 50)
    password = models.CharField(max_length = 255,widget= PasswordInput)
    email =  models.EmailField(max_length = 200)


    class Meta:
        abstract = True