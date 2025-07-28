from django.shortcuts import render,redirect, HttpResponse
from custom_user_app.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
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

        if password == confirm_password:
            user = customUser.objects.create_user(
                image = image,
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
    logout(request)
    return redirect('loginPage')
@login_required
def home(request):
    userData = customUser.objects.all()
    return render(request, 'home.html', {'users': userData})
def addUser(request):
    return render(request, 'addUser.html')
def editUser(request,id):
    return render(request, 'editUser.html')
def viewUser(request,id):
    return render(request, 'viewUser.html')
def deleteUser(request,id):
    customUser.objects.get(id=id).delete()
    return redirect('home')