from django.urls import path
from employer_app.views import *

urlpatterns = [
    path('addJob/', addJob, name='addJob'),
    path('jobListPage/', jobListPage, name='jobListPage'),
    path('editJob/<str:id>', editJob, name='editJob'),
]