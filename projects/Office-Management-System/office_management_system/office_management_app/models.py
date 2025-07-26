from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    user_type = models.CharField(choices=[('Admin','Admin'),('Employee','Employee')],max_length=100, null=True)
    def __str__(self):
        return self.username
    

class DepartmentModel(models.Model):
    department_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return self.department_name
    

    
class EmployeeManagementModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE, null=True, related_name='department_info')
    full_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    join_date = models.DateField(null=True)
    profile = models.ImageField(upload_to='media/profile',null=True)
    def __str__(self):
        return self.full_name
    
    
class LeaveModel(models.Model):
    employee = models.ForeignKey(EmployeeManagementModel,on_delete=models.CASCADE,null=True, related_name='leave_info')
    leave_type = models.CharField(choices=[('Casual_leave','Casual_leave'),('Sick_leave','Sick_leave'),('Annual_leave','Annual_leave'),('Paternity_leave','Paternity_leave')],max_length=100, null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    reason = models.TextField(null=True)
    status = models.CharField(choices=[('Pending','Pending'),('Approved','Approved'),('Rejected','Rejected')],max_length=100, null=True)
    def __str__(self):
        return self.employee.full_name