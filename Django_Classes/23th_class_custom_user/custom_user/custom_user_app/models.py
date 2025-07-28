from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUser(AbstractUser):
    role =[
        ('seeker', "Seeker"),
        ('rectuiter', "Recruiter"),

    ]
    image = models.ImageField(upload_to='media/images', null=True)
    user_type = models.CharField(choices=role, max_length=100, null=True)
    age = models.PositiveIntegerField(null=True)
    mobile = models.CharField(max_length=17, null=True)
    description = models.TextField(null=True)
    instutite = models.CharField(max_length=100, null=True)
    passingYear = models.IntegerField(null=True)
    experience = models.PositiveSmallIntegerField(null=True)

