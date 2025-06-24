from django.db import models

# Create your models here.
class taskModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    dueDate = models.CharField(max_length=100)

class userModel(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100, null=True)
    userName = models.CharField(max_length=100, null=True)
    