from django.db import models

# Create your models here.
class recipeModel(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=200, null=True)
    ingredients = models.TextField(max_length=200, null=True)
    instructions = models.TextField(max_length=200, null=True)
    image = models.ImageField(upload_to='media/recipe', null=True)
