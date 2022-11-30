from django.db import models

# Create your models here.

class registered_courses (models.Model):
    course_id = models.IntegerField()
    professor_id = models.IntegerField()

class registered_students_in_a_course (models.Model):
    course_id = models.IntegerField()
    professor_id = models.IntegerField()
    student_id = models.IntegerField()
    grade = models.CharField(max_length=50)

    
