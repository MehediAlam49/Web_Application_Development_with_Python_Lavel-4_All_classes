from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customUserModel(AbstractUser):
    USER_TYPE = [
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
    ]
    user_type = models.CharField(choices=USER_TYPE, max_length=100, null=True, blank=True)


class teacherModel(models.Model):
    user = models.OneToOneField(customUserModel, on_delete=models.CASCADE, null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    hire_date = models.DateField(null=True,blank=True)
    def __str__(self):
        return str(self.user)

class studentModel(models.Model):
    teacher = models.ForeignKey(teacherModel, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    Last_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=100, null=True, blank=True)
    enrollment_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return str(self.teacher)