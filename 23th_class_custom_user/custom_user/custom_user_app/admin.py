from django.contrib import admin
from custom_user_app.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class customuserAdmin(UserAdmin):
    list_display=['username', 'email', 'user_type', 'age', 'mobile', 'description', 'image', 'instutite', 'passingYear', 'experience']

admin.site.register(customUser,customuserAdmin)