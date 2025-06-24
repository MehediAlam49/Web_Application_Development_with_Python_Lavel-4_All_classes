from django.db import models

# Create your models here.
class customerModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.BigIntegerField()
    address = models.TextField()
    
class productModel(models.Model):
    product_name = models.CharField(max_length=100)
    Product_details = models.CharField()
    price = models.BigIntegerField()
    Quality = models.IntegerField()
    created_date = models.DateField()
