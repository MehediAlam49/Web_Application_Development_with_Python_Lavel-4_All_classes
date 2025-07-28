from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    user_type= models.CharField(choices=[('Job_seeker','Job_seeker'),('Recruiter','Recruiter')],max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.username
    

class JobModel(models.Model):
    job_title= models.CharField(max_length=100,null=True)
    description= models.TextField(null=True)
    salary= models.PositiveBigIntegerField(null=True)
    location= models.CharField(max_length=100,null=True)
    deadline= models.DateField(null=True)
    def __str__(self):
        return self.job_title