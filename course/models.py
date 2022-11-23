from django.db import models

# Create your models here.

# declare a new model with a name "Course"
class Course(models.Model):
    # fields of the model
    name = models.TextField()
    code = models.TextField()
    section = models.TextField()
    units = models.TextField()
    timetable = models.TextField()
    location = models.TextField()
    instructor = models.TextField()
    course_dates = models.TextField()
    status = models.TextField()
    capacity = models.TextField()
    description = models.TextField(default='N/A')
    last_modified = models.DateTimeField(auto_now_add = True)