from django.shortcuts import render, redirect,HttpResponse
from project.models import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            userData = customUserModel.objects.create_user(

                username=username,
                email=email,
                
                password=confirm_password,
            )
            if userData:
                user = studentModel.objects.create(
                    user = userData,
                    student_name=student_name,
                    student_id=student_id,
                )
            userData.save()
            return redirect(loginPage)
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


def home(request):
    user =request.user
    if user.is_superuser:
        projectData = projectModel.objects.all()
    else:
        projectData = projectModel.objects.filter(user=request.user)
    return render(request, 'home.html', {'project':projectData})

def projectList(request):
    projectData = projectModel.objects.filter(user = request.user)
    return render(request, 'projectList.html', {'projects': projectData})


def addProject(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        project_description = request.POST.get('project_description')
        deadline = request.POST.get('deadline')
        created_by = request.POST.get('created_by')
        project_status = request.POST.get('project_status')

        projectData = projectModel.objects.create(
            user = request.user,
            project_name=project_name,
            project_description=project_description,
            deadline=deadline,
            created_by=created_by,
            project_status=project_status,
        )
        projectData.save()
        return redirect('projectList')
    return render(request, 'addProject.html')
def viewProject(request,id):
    projectData = projectModel.objects.get(id=id)
    return render(request, 'viewProject.html', {'projects': projectData})
def editProject(request,id):
    projectData = projectModel.objects.get(id=id)
    if request.method == 'POST':
        projectData.project_name = request.POST.get('project_name')
        projectData.project_description = request.POST.get('project_description')
        projectData.deadline = request.POST.get('deadline')
        projectData.created_by = request.POST.get('created_by')
        projectData.project_status = request.POST.get('project_status')

        projectData.save()
        return redirect('projectList')
    return render(request, 'editProject.html', {'projects':projectData})
def deleteProject(request,id):
    projectModel.objects.get(id=id).delete()
    return redirect('projectList')



def changeStatus(request,id):
    status = projectModel.objects.get(id=id)
    if status.project_status == 'NotStarted':
        status.project_status = 'InProgress'
    elif status.project_status == 'InProgress':
        status.project_status = 'Completed'
    status.save()
    return redirect('projectList')