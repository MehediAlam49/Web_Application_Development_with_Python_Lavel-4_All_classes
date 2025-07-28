from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customUserModel(AbstractUser):
    image = models.ImageField(upload_to='media/users_profile', null=True)
    full_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=18, null=True)
    address = models.CharField(max_length=100, null=True)
    city_name = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class itemModel(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('in_progress','In_progress'),
        ('completed','Completed'),
    ]
    user = models.ForeignKey(customUserModel, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
