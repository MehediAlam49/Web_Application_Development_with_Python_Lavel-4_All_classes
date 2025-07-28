from django.db import models

# Create your models here.
class studentModel(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    date = models.DateField()

class bookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField()
    price = models.IntegerField()
    stock = models.IntegerField()
