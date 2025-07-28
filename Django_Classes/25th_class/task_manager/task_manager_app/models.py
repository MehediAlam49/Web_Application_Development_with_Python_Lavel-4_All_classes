from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customUserModel(AbstractUser):
    profile_image = models.ImageField(upload_to='media/profiles', null=True)
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)


class taskModel(models.Model):
    user=models.ForeignKey(customUserModel, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    due_date = models.DateField(null=True)
    priority = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)