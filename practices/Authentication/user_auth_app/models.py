from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    user_type = models.CharField(choices=[('Admin','Admin'),('Guest','Guest'),],max_length=100,null=True)
    def __str__(self):
        return self.username