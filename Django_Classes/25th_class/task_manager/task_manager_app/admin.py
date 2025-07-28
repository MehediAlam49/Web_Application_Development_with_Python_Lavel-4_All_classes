from django.contrib import admin
from task_manager_app.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class customUserAdmin(UserAdmin):
    list_display=['username', 'full_name', 'email', 'bio']

admin.site.register(customUserModel, customUserAdmin)

admin.site.register(taskModel)