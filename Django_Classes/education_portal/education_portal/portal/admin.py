from django.contrib import admin
from portal.models import *

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(TeacherModel)
admin.site.register(StudentBasicInfoModel)
admin.site.register(EducationInfoModel)