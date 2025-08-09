
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from schoolApp.models import *

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user_type = request.POST.get('uer_type')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            CustomUserModel.objects.create_user(
                username=username,
                email=email,
                phone=phone,
                user_type=user_type,
                password=confirm_password,
            )
            return redirect('loginPage')
    return render(request, 'signupPage.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'loginPage.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def home(request):
    return render(request, 'home.html')

def addTeacher(request):
    return render(request, 'addTeacher.html')