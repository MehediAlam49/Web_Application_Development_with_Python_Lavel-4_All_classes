from django.contrib import admin
from to_do_app.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class customUserAdmin(UserAdmin):
    list_display = ['username', 'email']

admin.site.register(customUserModel, customUserAdmin)

admin.site.register(itemModel)