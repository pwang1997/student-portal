from django.db import models

# Create your models here.

# declare a new model with a name "Course"
class Course(models.Model):
        # fields of the model
    Course_ID =  models.TextField()
    Course_name = models.TextField()
    Course_code = models.TextField()
    Section = models.TextField()
    Units = models.TextField()
    Days_and_time = models.TextField()
    Room = models.TextField()
    Instructor = models.TextField()
    Meeting_Dates = models.TextField()
    Status = models.TextField()
    Capacity = models.TextField()
    Course_description = models.TextField(default='N/A')

    last_modified = models.DateTimeField(auto_now_add = True)
    
  
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title