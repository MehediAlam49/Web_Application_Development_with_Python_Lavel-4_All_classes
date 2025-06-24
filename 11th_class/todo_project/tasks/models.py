from django.db import models

# Create your models here.
class taskModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    dueDate = models.CharField(max_length=100)