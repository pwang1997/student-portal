import email
from gzip import FNAME
from django.db import models
from user.models import Users

# Create your models here.
class Student(Users):
    major = models.CharField(max_length = 255)

class Enrolled_courses_of_a_student (models.Model):
    course_id = models.IntegerField()
    professor_id = models.IntegerField()
    student_id = models.IntegerField()
    grade = models.CharField(max_length=50)

