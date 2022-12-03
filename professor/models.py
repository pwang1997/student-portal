from django.db import models
from django.forms import IntegerField
from user.models import Users


class registered_courses (models.Model):
    course_id = models.IntegerField()
    professor_id = models.IntegerField()

class registered_students_in_a_course (models.Model):
    course_id = models.IntegerField()
    professor_id = models.IntegerField()
    student_id = models.IntegerField()
    grade = models.CharField(max_length=50)

   
class Professor(Users):
      department = models.CharField(max_length = 255)
      salary = IntegerField()