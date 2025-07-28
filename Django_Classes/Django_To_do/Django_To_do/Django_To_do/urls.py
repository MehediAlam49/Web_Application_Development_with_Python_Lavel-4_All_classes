
from django.contrib import admin
from django.urls import path
from to_do_app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signupPage, name='signupPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('home/', home, name='home'),
    path('itemList/', itemList, name='itemList'),

    path('addItem/', addItem, name='addItem'),
    path('editItem/<str:id>', editItem, name='editItem'),
    path('viewItem/<str:id>', viewItem, name='viewItem'),
    path('deleteItem/<str:id>', deleteItem, name='deleteItem'),

    path('passwordNotMatched/', passwordNotMatched, name='deleteItem'),
    path('passwordWrong/', passwordWrong, name='passwordWrong'),
    path('changePassword/', changePassword, name='changePassword'),
    path('statusChange/<str:id>', statusChange, name='statusChange'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
