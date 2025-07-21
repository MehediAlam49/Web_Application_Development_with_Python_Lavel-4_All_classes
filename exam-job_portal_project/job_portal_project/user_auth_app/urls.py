from django.urls import path
from user_auth_app.views import *

urlpatterns = [
    path('', registerPage, name='registerPage'),
    path('login/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('home/', homePage, name='homePage'),
    path('profileInfo/', profileInfo, name='profileInfo'),
    path('editProfile/<str:id>', editProfile, name='editProfile'),
    path('pendingListPage/', pendingListPage, name='pendingListPage'),
    path('acceptPendingaccount/<str:id>', acceptPendingaccount, name='acceptPendingaccount'),
    path('changePasswordPage/', changePasswordPage, name='changePasswordPage'),

]