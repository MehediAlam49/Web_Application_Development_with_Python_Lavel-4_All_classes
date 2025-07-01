from django.shortcuts import render,redirect,HttpResponse
from task_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            CustumUserModel.objects.create_user(
                username=username,
                profile_picture = profile_image,
                first_name=full_name,
                email=email,
                bio=bio,
                password=confirm_password,
            )
            return redirect('loginPage')
    return render(request, 'registerPage.html')
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('username or password not matched')
    return render(request, 'loginPage.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')


@login_required
def home(request):
    total = taskModel.objects.filter(user = request.user)
    inProgressData = taskModel.objects.filter(user = request.user, status = 'in_progress')
    pendingData = taskModel.objects.filter(user = request.user, status = 'pending')
    completedData = taskModel.objects.filter(user = request.user, status = 'completed')
    return render(request, 'home.html', {'total':total, 'inProgressData': inProgressData, 'pendingData':pendingData, 'completedData': completedData})

@login_required
def taskList(request):
    taskData = taskModel.objects.filter(user = request.user )
    return render(request, 'taskList.html', {'tasks': taskData})

@login_required
def addTask(request):
    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        status = request.POST.get('status')

        taskModel.objects.create(
            user = request.user,
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            status=status,
        )
        return redirect('taskList')
    return render(request, 'addTask.html')

def editTask(request,id):
    taskData = taskModel.objects.get(id=id)
    if request.method == 'POST':
        taskData.user = request.user
        taskData.title = request.POST.get('title')
        taskData.description = request.POST.get('description')
        taskData.due_date = request.POST.get('due_date')
        taskData.priority = request.POST.get('priority')
        taskData.status = request.POST.get('status')

        taskData.save()
        return redirect('taskList')
    return render(request, 'editTask.html', {'task': taskData})

def viewTask(request,id):
    taskData = taskModel.objects.get(id=id)
    return render(request, 'viewTask.html', {'task': taskData})
def deleteTask(request,id):
    return render(request, 'deleteTask.html')


def changePasswordPage(request):
    current_user = request.user
    if request.method == 'POST':
        oldPassword = request.POST.get('oldPassword')
        newPassword = request.POST.get('newPassword')
        confirmPassword = request.POST.get('confirmPassword')

        if check_password(oldPassword, current_user.password):
            if newPassword == confirmPassword:
                current_user.set_password(newPassword)
                current_user.save()
                update_session_auth_hash(request,current_user)
                return redirect('home')
    return render(request, 'changePasswordPage.html')


def changeStatus(request,id):
    taskData = taskModel.objects.get(id=id)
    if taskData.status == 'pending':
        taskData.status = 'in_progress'
    elif taskData.status == 'in_progress':
        taskData.status = 'completed'
    taskData.save()
    return redirect('taskList')

def changePriority(request,id):
    taskData = taskModel.objects.get(id=id)
    if taskData.priority == 'low':
        taskData.priority = 'medium'
    elif taskData.priority == 'medium':
        taskData.priority = 'high'
    taskData.save()
    return redirect('taskList')