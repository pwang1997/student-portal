from django.db import models

class Course (models.Model):
    description = models.CharField(max_length=100)
    prerequisite = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    code = models.IntegerField()
    section = models.IntegerField()
