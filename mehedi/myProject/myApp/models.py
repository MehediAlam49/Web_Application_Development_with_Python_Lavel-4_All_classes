from django.db import models

# Create your models here.
class studentModel(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    birth_date=models.DateField()
    address=models.TextField()
    
class newstudentModel(models.Model):
    student=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    age=models.IntegerField()