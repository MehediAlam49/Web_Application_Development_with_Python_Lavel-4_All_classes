from django.contrib import admin
from office_management_app.models import *

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(DepartmentModel)
admin.site.register(EmployeeManagementModel)
admin.site.register(LeaveModel)