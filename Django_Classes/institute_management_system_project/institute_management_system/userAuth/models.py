from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustumUserModel(AbstractUser):
    user_type = models.CharField(choices=[('Admin','Admin'),('Teacher','Teacher'),('Student','Student')],max_length=100, null=True)
    def __str__(self):
        return self.username
    

class TeacherModel(models.Model):
    teacher_user = models.OneToOneField(CustumUserModel, on_delete=models.CASCADE, null=True,related_name = 'teacher_info')
    teacher_name  = models.CharField(max_length=100,null=True)
    teacher_phone  = models.CharField(max_length=100,null=True)
    teacher_profile  = models.ImageField(upload_to='media/teachers',null=True)

    def __str__(self):
        return self.teacher_name
    

class StudentModel(models.Model):
    student_user = models.OneToOneField(CustumUserModel, on_delete=models.CASCADE, null=True,related_name = 'teacher_info')
    teacher_name  = models.CharField(max_length=100,null=True)
    teacher_phone  = models.CharField(max_length=100,null=True)
    teacher_profile  = models.ImageField(upload_to='media/teachers',null=True)

    def __str__(self):
        return self.teacher_name

