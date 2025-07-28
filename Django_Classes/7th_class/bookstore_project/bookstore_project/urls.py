
from django.contrib import admin
from django.urls import path
from bookstore_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('books/', books, name='books'),
    path('user/', user, name='user'),
    path('addStudent/', addStudent, name='addStudent'),
    path('studentList/', studentList, name='studentList'),
]
