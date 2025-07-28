from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    user_type = models.CharField(choices=[('Admin', 'Admin'),('Teacher','Teacher')])

    def __str__(self):
        return self.username
    

class TeacherModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE,null=True)
    subject = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)

class StudentModel(models.Model):
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(null=True)
    grade = models.CharField(max_length=100, null=True)
    enrolment_date = models.DateTimeField(auto_now_add=True, null=True)