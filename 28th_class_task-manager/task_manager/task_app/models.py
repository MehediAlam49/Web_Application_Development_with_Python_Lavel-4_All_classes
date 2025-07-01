from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustumUserModel(AbstractUser):
    profile_picture = models.ImageField(upload_to='media/profile', null=True)
    bio = models.TextField(null=True)


class taskModel(models.Model):
    my=[
        ('pending','Pending'),
        ('in_progress','InProgress'),
        ('completed','Completed'),
    ]
    user = models.ForeignKey(CustumUserModel, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    due_date = models.DateField(null=True)
    priority = models.CharField(choices=[('low','Low'),('medium','Medium'),('high','High')], max_length=100, null=True)
    status = models.CharField(choices=my, max_length=100, null=True)