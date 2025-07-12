from django.contrib import admin
from management.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ['user_type']

admin.site.register(CustomUserModel, CustomUserAdmin)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)