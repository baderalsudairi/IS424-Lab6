from django.db import models
# myapp/models.py
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name='students')
    # Add other fields as needed
