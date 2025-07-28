
from django.contrib import admin
from django.urls import path
from LibraryApp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('changePasswordPage/', changePasswordPage, name='changePasswordPage'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('editProfile/', editProfile, name='editProfile'),
    path('addBook/', addBook, name='addBook'),
    path('viewBook/<str:id>', viewBook, name='viewBook'),
    # path('editBook/<str:id>', editBook, name='editBook'),
    path('deleteBook/<str:id>', deleteBook, name='deleteBook'),
    path('bookListPage/', bookListPage, name='bookListPage'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
