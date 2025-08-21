from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login, logout
from user_auth_app.models import *

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        profile = request.FILES.get('profile')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            CustomUserModel.objects.create_user(
                username=username,
                profile=profile,
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
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'loginPage.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def changePasswordPage(request):
    return render(request, 'changePasswordPage.html')

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')