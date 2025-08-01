from django.db import models

# Create your models here.

class StudentModel(models.Model):
    student_name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    roll = models.PositiveBigIntegerField(null=True)
    username = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100,null=True)
    register_date = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.student_name



class TeacherModel(models.Model):
    teacher_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=100,null=True)
    designation = models.CharField(max_length=50, null=True)
    images = models.ImageField(upload_to='media/images',null=True)
    def __str__(self):
        return self.teacher_name