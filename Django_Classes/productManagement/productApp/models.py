from django.db import models

# Create your models here.
class productModel(models.Model):
    product_name = models.CharField(max_length=100)
    product_details = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity =models.IntegerField()
    created_date = models.DateField()


class customerModel(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField()
    contact = models.IntegerField()
    address = models.TextField()
