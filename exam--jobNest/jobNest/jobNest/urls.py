
from django.contrib import admin
from django.urls import path
from jobNestApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('homePage/', homePage, name='homePage'),
    path('profileInfo/', profileInfo, name='profileInfo'),
    # path('editProfile/', editProfile, name='editProfile'),
    path('changePasswordPage/', changePasswordPage, name='changePasswordPage'),
    path('addJob/', addJob, name='addJob'),
]
