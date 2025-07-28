from django.shortcuts import render,redirect
from management.models import *
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupPage(request):
    return render(request, 'signupPage.html')