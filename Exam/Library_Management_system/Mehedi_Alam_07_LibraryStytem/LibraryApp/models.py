from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    user_type =models.CharField(choices=[('Student','Student'),('Librarian','Librarian')],max_length=100,null=True)
    def __str__(self):
        return self.username

class BookModel(models.Model):
    title = models.CharField(max_length=100,null=True)
    author = models.CharField(max_length=100,null=True)
    isbn = models.CharField(max_length=100,null=True)
    quantity = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title

class StudentProfileModel(models.Model):
    student_id = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,null=True)
    department = models.CharField(max_length=100,null=True)
    contact_number = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    profile = models.ImageField(upload_to='media/profile',null=True)
    
    
class LibrarianProfileModel(models.Model):
    employee_id = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,null=True)
    designation = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    profile = models.ImageField(upload_to='media/profile',null=True)
    