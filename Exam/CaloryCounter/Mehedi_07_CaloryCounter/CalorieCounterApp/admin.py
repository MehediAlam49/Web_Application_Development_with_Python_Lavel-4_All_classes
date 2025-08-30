from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(UserProfileModel)
admin.site.register(DailyCalorieConsumedModel)
admin.site.register(TotalConsumedModel)