from django.shortcuts import render,redirect,HttpResponse
from task_manager_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        bio = request.POST.get('bio')

        if password == confirm_password:
            user = customUserModel.objects.create_user(
                profile_image=profile_image,
                username=username,
                full_name=full_name,
                email=email,
                password=confirm_password,
                bio = bio,
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
    return render(request, 'loginPage.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required
def home(request):
    return render(request, 'home.html')
@login_required
def taskList(request):
    taskData = taskModel.objects.filter(user=request.user)
    return render(request, 'taskList.html', {'task': taskData})

@login_required
def addTask(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        status = request.POST.get('status')

        task = taskModel.objects.create(
            user = request.user,
            title = title,
            description = description,
            due_date = due_date,
            priority = priority,
            status = status,
        )
        return redirect('taskList')

    return render(request, 'addTask.html')
@login_required
def editTask(request, id):
    taskData = taskModel.objects.get(id=id)
    if request.method == 'POST':
        taskData.title = request.POST.get('title')
        taskData.description = request.POST.get('description')
        taskData.due_date = request.POST.get('due_date')
        taskData.priority = request.POST.get('priority')
        taskData.status = request.POST.get('status')

        taskData.save()
        return redirect(taskList)

    return render(request, 'editTask.html', {'task': taskData})
@login_required
def viewTask(request, id):
    taskData = taskModel.objects.get(id=id)
    return render(request, 'viewTask.html', {'task': taskData})
@login_required
def deleteTask(request, id):
    taskModel.objects.get(id=id).delete()
    return redirect('taskList')