from django.db import models
from django.forms import IntegerField
from user.models import Users


class registered_courses (models.Model):
    course_id = models.IntegerField()
    professor_id = models.IntegerField()
   
class Professor(Users):
      department = models.CharField(max_length = 255)
      salary = IntegerField()