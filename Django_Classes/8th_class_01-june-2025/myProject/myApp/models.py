from django.db import models

# Create your models here.
class studentModel(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField()

class teacherModel(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField()

class courseModel(models.Model):
    title = models.CharField(max_length=100)
    course_code = models.IntegerField()
    semester = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
