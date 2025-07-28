from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customUserModel(AbstractUser):
    email = models.EmailField(null=True,blank=True)

class studentModel(models.Model):
    user = models.OneToOneField(customUserModel, on_delete=models.CASCADE, null=True)
    student_name = models.CharField(max_length=100, null=True,blank=True)
    student_id = models.IntegerField( null=True,blank=True)

class projectModel(models.Model):
    user = models.ForeignKey(customUserModel, on_delete=models.CASCADE, null=True)
    PROJECT_STATUS = [
        ('NotStarted', 'NotStarted'),
        ('InProgress', 'InProgress'),
        ('Completed', 'Completed'),
    ]
    project_name = models.CharField(max_length=100,null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)
    project_status = models.CharField(choices=PROJECT_STATUS,max_length=100, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)