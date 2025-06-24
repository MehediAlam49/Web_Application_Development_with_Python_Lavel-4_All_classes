from django.shortcuts import render, redirect
from user_auth.models import userAuthModel

# Create your views here.
def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            userinfo =userAuthModel.objects.create(
            username = username,
            fullname = fullname,
            email = email,
            contact = contact,
            password = password
            )
            userinfo.save()
            return redirect('login')
        else:
            print('password not match')
    
    return render(request, 'register.html')