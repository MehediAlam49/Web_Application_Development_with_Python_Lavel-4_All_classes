from django.shortcuts import render,redirect, HttpResponse
from custom_user_app.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')
        age = request.POST.get('age')
        mobile = request.POST.get('mobile')
        description = request.POST.get('description')
        instutite = request.POST.get('instutite')
        passingYear = request.POST.get('passingYear')
        experience = request.POST.get('experience')
        image = request.FILES.get('image')

        if password == confirm_password:
            user = customUser.objects.create_user(
                username=username,
                email=email,
                password=confirm_password,
                user_type=role,
                age=age,
                mobile=mobile,
                description=description,
                instutite=instutite,
                passingYear=passingYear,
                experience=experience,
                image = image,

            )
            return redirect(loginPage)
    return render(request, 'signupPage.html')
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password = password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('username or pass not matched')

    return render(request, 'loginPage.html')
def logoutPage(request):
    return render(request, 'logoutPage.html')
def home(request):
    return render(request, 'home.html')