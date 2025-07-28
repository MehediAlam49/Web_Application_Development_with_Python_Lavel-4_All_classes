from django.db import models

# Create your models here.
class recipeModel(models.Model):
    image = models.ImageField(upload_to='media/resume')
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()