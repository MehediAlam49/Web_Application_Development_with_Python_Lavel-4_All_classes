from django.urls import path
from employer_app.views import *

urlpatterns = [
    path('addJob/', addJob, name='addJob')
]