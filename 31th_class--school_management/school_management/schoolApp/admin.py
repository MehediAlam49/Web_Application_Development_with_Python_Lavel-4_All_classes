from django.contrib import admin
from schoolApp.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class custumUserAdmin(UserAdmin):
    list_display = ['username', 'user_type']


admin.site.register(customUserModel, custumUserAdmin)
admin.site.register(teacherModel)
admin.site.register(studentModel)