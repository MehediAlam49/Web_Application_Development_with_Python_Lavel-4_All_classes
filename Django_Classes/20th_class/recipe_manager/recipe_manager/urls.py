
from django.contrib import admin
from django.urls import path
from recipe.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', loginPage, name='loginPage'),
    path('signupPage/', signupPage, name='signupPage'),
    path('wrongPassword/', wrongPassword, name='wrongPassword'),
    path('passwordError/', passwordError, name='passwordError'),
    path('logoutPage/', logoutPage, name='logoutPage'),



    path('addRecipe/', addRecipe, name='addRecipe'),
    path('editRecipe/<str:id>', editRecipe, name='editRecipe'),
    path('viewRecipe/<str:id>', viewRecipe, name='viewRecipe'),
    path('deleteRecipe/<str:id>', deleteRecipe, name='deleteRecipe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
