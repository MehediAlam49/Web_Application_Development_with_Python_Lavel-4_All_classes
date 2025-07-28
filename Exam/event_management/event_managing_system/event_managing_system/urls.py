
from django.contrib import admin
from django.urls import path
from booking.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage,name='registerPage'),
    path('loginPage/', loginPage,name='loginPage'),
    path('logoutPage/', logoutPage,name='logoutPage'),

    path('home/', home,name='home'),
    path('profile/', profile,name='profile'),
    path('myBooking/', myBooking,name='myBooking'),

    path('addBooking/', addBooking,name='addBooking'),
    path('editBooking/<str:id>', editBooking,name='editBooking'),
    path('viewBooking/<str:id>', viewBooking,name='viewBooking'),
    path('deleteBooking/<str:id>', deleteBooking,name='deleteBooking'),
    path('statusChange/<str:id>', statusChange,name='statusChange'),

    path('changePasswordPage/', changePasswordPage,name='changePasswordPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
