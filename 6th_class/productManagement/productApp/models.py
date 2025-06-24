from django.db import models

# Create your models here.
class productModel(models.Model):
    product_name = models.CharField(max_length=100)
    product_details = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created_date = models.DateField()

class customerModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    address = models.TextField()