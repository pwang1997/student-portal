import email
from gzip import FNAME
from django.db import models
from user.models import Users

# Create your models here.


class Student(Users):
    major = models.CharField(max_length = 255)