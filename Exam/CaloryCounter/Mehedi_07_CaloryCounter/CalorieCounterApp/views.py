from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.
def register_view(request):
    return render(request, 'signup.html')
def login_view(request):
    return render(request, 'login.html')
def logout_view(request):
    return redirect('logon_view')
def home(request):
    return render(request, 'home.html')