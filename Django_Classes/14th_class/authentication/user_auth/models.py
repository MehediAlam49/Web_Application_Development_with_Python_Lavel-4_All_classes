from django.db import models

# Create your models here.
class userAuthModel(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)