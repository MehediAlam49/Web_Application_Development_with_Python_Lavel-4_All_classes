from django.contrib import admin
from auth_crud_app.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class customUserAdmin(UserAdmin):
    list_display=['profile_image', 'username', 'email', 'user_type', 'full_name', 'dob']

admin.site.register(customUserModel,customUserAdmin)

admin.site.register(productModel)