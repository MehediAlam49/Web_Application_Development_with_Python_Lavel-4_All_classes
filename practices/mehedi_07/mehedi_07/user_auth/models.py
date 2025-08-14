from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    full_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20,null=True)
    user_type = models.CharField(choices=[('Client','Client'),('Guest','Guest')],null=True)
    def __str__(self):
        return self.username