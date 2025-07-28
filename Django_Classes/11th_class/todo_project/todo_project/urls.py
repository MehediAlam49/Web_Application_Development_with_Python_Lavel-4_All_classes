
from django.contrib import admin
from django.urls import path
from todo_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addTask/', addTask, name='addTask'),
    path('editTask/<str:id>', editTask, name='editTask'),
    path('deleteTask/<str:id>', deleteTask, name='deleteTask'),
    path('viewTask/', viewTask, name='viewTask'),
    path('taskList/', taskList, name='taskList'),
]
