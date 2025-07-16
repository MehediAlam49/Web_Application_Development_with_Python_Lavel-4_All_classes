from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    USER_TYPE = [
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
    ]

    user_type = models.CharField(choices=USER_TYPE, max_length=100, null=True)


class TeacherModel(models.Model):
    teacher_name = models.CharField(max_length=100, null=True)
    last_education = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)


class StudentBasicInfoModel(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)


class EducationInfoModel(models.Model):
    student = models.ForeignKey(StudentBasicInfoModel, on_delete=models.CASCADE, null=True)
    degree_name = models.CharField(max_length=100, null=True)
    grade = models.CharField(max_length=100, null=True)
    passing_year = models.PositiveBigIntegerField(null=True)

