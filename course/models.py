from django.db import models

# declare a new model with a name "Course"
class Course(models.Model):
    # fields of the model
    name = models.TextField()
    department = models.CharField(max_length=50)
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
    prerequisite = models.CharField(max_length=100)
    last_modified = models.DateTimeField(auto_now_add = True)
