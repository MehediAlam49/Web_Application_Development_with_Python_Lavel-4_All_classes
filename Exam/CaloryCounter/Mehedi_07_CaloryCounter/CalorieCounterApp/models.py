from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    def __str__(self):
        return self.username
    
class  UserProfileModel(models.Model):
    GENDER_TYPE = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='user_profile')
    Name = models.CharField(max_length=100, null=True)
    Age = models.PositiveBigIntegerField(null=True)
    Gender = models.CharField(choices=GENDER_TYPE,max_length=100, null=True)
    Height = models.FloatField(null=True)
    Weight = models.FloatField(null=True)
    def __str__(self):
        return f"{self.user.username}-{self.Name}"
    
class DailyCalorieConsumedModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE,related_name='daily_calorie_consumed')
    Item_name = models.CharField(max_length=100, null=True)
    Calorie = models.FloatField(null=True)
    Date = models.DateField(null=True)
    def __str__(self):
        return f"{self.user.username}-{self.Item_name}-{self.Calorie}"
    
    
class TotalConsumedModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE,related_name='total_calorie_consumed')
    Total_consumed = models.FloatField(null=True)
    Date = models.DateField(null=True)
    def __str__(self):
        return f"{self.user.username}-{self.Total_consumed}"