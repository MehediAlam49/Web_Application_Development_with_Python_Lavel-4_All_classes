
from django.contrib import admin
from django.urls import path
from schoolApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage,name='registerPage'),
    path('loginPage/', loginPage,name='loginPage'),
    path('logoutPage/', logoutPage,name='logoutPage'),
    path('changePasswordPage/', changePasswordPage,name='changePasswordPage'),
    path('home/', home,name='home'),
    path('addStudent/', addStudent,name='addStudent'),
    path('studentList/', studentList,name='studentList'),
    path('viewStudent/<str:id>', viewStudent,name='viewStudent'),
    path('editStudent/<str:id>', editStudent,name='editStudent'),
    path('deleteStudent/<str:id>', deleteStudent,name='deleteStudent'),
]
