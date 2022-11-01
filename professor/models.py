from django.db import models
from django.forms import IntegerField
from user.models import Users

class Professor(Users):
      department = models.CharField(max_length = 255)
      salary = IntegerField()