from django.urls import path
from user_auth_app.views import *

urlpatterns = [
    path('', register, name='register')
    path('loginPage/', loginPage, name='loginPage')
    path('logoutPage/', logoutPage, name='logoutPage')
    path('home/', home, name='home')
]
