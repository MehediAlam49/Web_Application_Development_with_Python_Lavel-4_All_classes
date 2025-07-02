
from django.contrib import admin
from django.urls import path
from project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', loginPage, name='logoutPage'),

    path('home/',home, name='home'),
    path('projectList/',projectList, name='projectList'),


    path('addProject/',addProject, name='addProject'),
    path('editProject/<str:id>',editProject, name='editProject'),
    path('viewProject/<str:id>',viewProject, name='viewProject'),
    path('deleteProject/<str:id>',deleteProject, name='deleteProject'),
    path('changeStatus/<str:id>',changeStatus, name='changeStatus'),
]
