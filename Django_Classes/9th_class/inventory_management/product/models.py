from django.db import models

# Create your models here.
class productModel(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(max_length=100)
