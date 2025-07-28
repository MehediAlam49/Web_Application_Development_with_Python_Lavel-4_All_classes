from django.db import models

# Create your models here.
class bookModel(models.Model):
    title = models.CharField(max_length=100)
    author =models.CharField(max_length=100)
    category =models.CharField(max_length=100)
    publish_date =models.DateField()
    description =models.CharField(max_length=100)
    cover_photo =models.ImageField(upload_to='media/photos')
