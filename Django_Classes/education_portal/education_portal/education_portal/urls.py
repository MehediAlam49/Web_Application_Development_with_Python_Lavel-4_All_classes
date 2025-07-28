
from django.contrib import admin
from django.urls import path
from portal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage,name='registerPage'),
    path('loginPage/', loginPage,name='loginPage'),
    path('logoutPage/', logoutPage,name='logoutPage'),

    path('home/', home,name='home'),
    path('add-teacher/', addTeacher, name='addTeacher'),
    path('teacher-list/', teacher_list, name='teacher_list'), 
    path('addStudent/', addStudent,name='addStudent'),
    path('studentList/', studentList,name='studentList'),
]
