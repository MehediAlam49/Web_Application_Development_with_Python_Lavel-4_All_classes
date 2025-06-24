"""
URL configuration for reviewProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reviewProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',Home,name='Home'),
    path('AddStudent/', AddStudent,name='AddStudent'),
    path('StudentList', StudentList,name='StudentList'),
    path('AddTeacher/', AddTeacher,name='AddTeacher'),
    path('TeacherList/', TeacherList,name='TeacherList'),
    path('CourseList/', CourseList,name='CourseList'),
    path('AddCourse/', AddCourse,name='AddCourse'),
    path('deleteStudent/<str:myid>', deleteStudent,name='deleteStudent'),
    path('deleteTeacher/<str:myid>', deleteTeacher,name='deleteTeacher'),
    path('deleteCourse/<str:myid>', deleteCourse,name='deleteCourse'),
    path('editStudent/<str:myid>', editStudent,name='editStudent'),
    path('editTeacher/<str:myid>', editTeacher,name='editTeacher'),
    path('editCourse/<str:myid>', editCourse,name='editCourse'),
]

