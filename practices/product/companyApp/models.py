from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    company_name = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.company_name
    
    
class ProductModel(models.Model):
    product_name = models.CharField(max_length=100, null=True)
    price = models.PositiveIntegerField( null=True)
    quantity = models.PositiveIntegerField( null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.product_name
    
    
class JobModel(models.Model):
    title = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    salary = models.PositiveIntegerField( null=True)
    deadline = models.DateField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title
    
class EmployeeModel(models.Model):
    employee_name = models.CharField(max_length=100, null=True)
    email = models.EmailField( null=True)
    department = models.CharField(choices=[('HR','HR'),('Manager','Manager'),('Staff','Staff'),], null=True)
    def __str__(self):
        return self.title