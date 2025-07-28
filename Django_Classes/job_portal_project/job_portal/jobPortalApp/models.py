from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customUserModel(AbstractUser):
    USER_TYPE = [
        ('Rectuiter','Rectuiter'),
        ('Seeker','Seeker'),
    ]

    full_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    bio = models.TextField(null=True,blank=True)
    user_type =models.CharField(choices=USER_TYPE, max_length=100, null=True, blank=True)


class jobModel(models.Model):
    JOB_TYPE = [
        ('Part_time','Part_time'),
        ('Full_time','Full_time'),
    ]
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='media/company_logo', null=True, blank=True)
    job_type = models.CharField(choices=JOB_TYPE, max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(customUserModel,max_length=100, on_delete=models.CASCADE, null=True)