
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    user_type = models.CharField(choices=[
        ('Admin','Admin'),
        ('Employer','Employer'),
        ('Candidate','Candidate'),
    ],max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.username
    
        
class PendingAccountModel(models.Model):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField( null=True)
    phone = models.CharField(max_length=100, null=True)
    user_type = models.CharField(choices=[
        ('Employer','Employer'),
        ('Candidate','Candidate'),
    ],max_length=20, null=True)
    pending_status = models.CharField(choices=[
        ('Pending','Pending'),
        ('Accept','Accept'),
        ('Rejected','Rejected'),
    ],max_length=20, null=True)
    def __str__(self):
        return self.username
