
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('addStudent/', addStudent, name="addStudent"),
    path('studentList/', studentList, name="studentList"),
    path('addTeacher/', addTeacher, name="addTeacher"),
    path('teacherList/', teacherList, name="teacherList"),
    path('addCourse/', addCourse, name="addCourse"),
    path('courseList/', courseList, name="courseList"),

    # Actions in Course List
    path('editCourse/<str:myid>', editCourse, name="editCourse"),
    path('deleteCourse/<str:myid>', deleteCourse, name="deleteCourse"),
    path('viewCourse/<str:myid>', viewCourse, name="viewCourse"),

    # Actions in Student List
    path('editStudent/<str:myid>', editStudent, name="editStudent"),
    path('deleteStudent/<str:myid>', deleteStudent, name="deleteStudent"),
    path('viewStudent/<str:myid>', viewStudent, name="viewStudent"),

    # Actions in Teacher List
    path('editTeacher/<str:myid>', editTeacher, name="editTeacher"),
    path('deleteTeacher/<str:myid>', deleteTeacher, name="deleteTeacher"),
    path('viewTeacher/<str:myid>', viewTeacher, name="viewTeacher"),

]
