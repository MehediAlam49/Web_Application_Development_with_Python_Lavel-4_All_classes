from django.urls import path
from user_auth_app.views import *


urlpatterns = [
    path('', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('changePasswordPage/', changePasswordPage, name='changePasswordPage'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
]
