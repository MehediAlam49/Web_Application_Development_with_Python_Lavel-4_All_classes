from django.contrib import admin
from task_app.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class customUserAdmin(UserAdmin):
    list_display=['username', 'email','bio']

admin.site.register(CustumUserModel, customUserAdmin)

admin.site.register(taskModel)