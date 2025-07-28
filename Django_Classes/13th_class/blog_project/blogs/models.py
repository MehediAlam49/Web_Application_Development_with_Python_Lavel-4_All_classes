from django.db import models

# Create your models here.
class userModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField()

class contentModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
