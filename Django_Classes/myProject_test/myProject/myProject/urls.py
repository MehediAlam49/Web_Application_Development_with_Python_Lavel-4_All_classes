
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewStudent/', viewStudent, name='viewStudent'),
    path('home/', homePage, name='homePage'),
    path('contact/', contactPage, name='contactPage'),
    path('news/', newsPage, name='newsPage'),
    path('about/', aboutPage, name='aboutPage'),
    
]
