
from django.contrib import admin
from django.urls import path
from jobPortalApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('home/', home, name='home'),
    path('jobFeed/', jobFeed, name='jobFeed'),
    path('addJob/', addJob, name='addJob'),
    path('editJob/<str:id>', editJob, name='editJob'),
    path('deleteJob/<str:id>', deleteJob, name='deleteJob'),

  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
