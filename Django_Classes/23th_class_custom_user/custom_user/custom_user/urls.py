
from django.contrib import admin
from django.urls import path
from custom_user_app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signupPage, name='signupPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('home/', home, name='home'),
    path('addUser/', addUser, name='addUser'),
    path('editUser/<str:id>', editUser, name='editUser'),
    path('viewUser/<str:id>', viewUser, name='viewUser'),
    path('deleteUser/<str:id>', deleteUser, name='deleteUser'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
