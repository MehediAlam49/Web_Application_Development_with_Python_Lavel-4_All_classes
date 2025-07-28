
from django.contrib import admin
from django.urls import path
from crud_1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('book/', book, name='book'),
    path('studentList/', studentList, name='studentList'),
    path('addBook/', addBook, name='addBook'),
    path('addStudent/', addStudent, name='addStudent'),
]
