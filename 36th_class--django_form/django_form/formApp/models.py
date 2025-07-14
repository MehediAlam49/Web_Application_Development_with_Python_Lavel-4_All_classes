from django.db import models

# Create your models here.
class UserInfoModel(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.full_name
    
class BasicInfoModel(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    profile = models.ImageField(upload_to='media/profile',null=True)
    def __str__(self):
        return self.full_name