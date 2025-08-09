from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    USER_TYPE = [
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE,default='Admin')

    def __str__(self):
        return self.username
    
class TeacherModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    designation = models.TextField(null=True)
    address = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
    
class TeacherModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    class_name = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
    
