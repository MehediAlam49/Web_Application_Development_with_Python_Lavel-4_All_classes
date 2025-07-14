
from django.contrib import admin
from django.urls import path
from formApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userInfoView, name='userInfoView'),
    path('home/', home, name='home'),
    path('basicInfoView/', basicInfoView, name='basicInfoView'),
]
