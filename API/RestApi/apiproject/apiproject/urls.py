
from django.contrib import admin
from django.urls import path
from apiApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentList/', studentList, name='studentList'),
    path('addStudent/', addStudent, name='addStudent'),
]
