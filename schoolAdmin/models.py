from django.db import models
from user.models import Users

# Create your models here.

class SchoolAdmin(Users):
    token = models.CharField(max_length=255)
