from django.db import models

# Create your models here.
class infoModel(models.Model):
    image = models.ImageField(upload_to='media/images', null=True)
    name = models.CharField(max_length=100, null=True)
    about = models.TextField(null=True)
    phone = models.CharField( max_length=17, null=True)