
from django.contrib import admin
from django.urls import path
from task_app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('home/', home, name='home'),
    path('taskList/', taskList, name='taskList'),
    path('addTask/', addTask, name='addTask'),
    path('editTask/<str:id>', editTask, name='editTask'),
    path('viewTask/<str:id>', viewTask, name='viewTask'),
    path('deleteTask/<str:id>', deleteTask, name='deleteTask'),
    path('changePasswordPage/', changePasswordPage, name='changePasswordPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
