
from django.contrib import admin
from django.urls import path
from office_management_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('addDepartment/', addDepartment, name='addDepartment'),
    path('departmentList/', departmentList, name='departmentList'),
    path('addEmployer/', addEmployer, name='addEmployer'),
    path('employerList/', employerList, name='employerList'),
    path('addLeave/', addLeave, name='addLeave'),
    path('leaveList/', leaveList, name='leaveList'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
