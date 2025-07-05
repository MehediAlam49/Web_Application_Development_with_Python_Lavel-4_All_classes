from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from schoolApp.models import *

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')

        if password == confirm_password:
            userData = customUserModel.objects.create_user(
                
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=confirm_password,
                user_type=user_type,
            )
            userData.save()
            if userData:
                teacherModel.objects.create(
                    user = userData,
                    subject=subject,
                    phone=phone,
                    hire_date=hire_date,

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

def changePasswordPage(request):
    current_user = request.user
    if request.method == 'POST':
        oldPassword = request.POST.get('oldPassword')
        newPassword = request.POST.get('newPassword')
        confirmPassword = request.POST.get('confirmPassword')

        if check_password(oldPassword,current_user.password):
            if newPassword == confirmPassword:
                current_user.set_password(newPassword)
                current_user.save()
                return redirect('home')

    return render(request, 'changePasswordPage.html')

def home(request):
    return render(request, 'home.html')
def addStudent(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        enrollment_date = request.POST.get('enrollment_date')
        teacher = teacherModel.objects.get(user=request.user)
        studentModel.objects.create(
            teacher = teacher,
            first_name=first_name,
            Last_name =last_name,
            age = age,
            grade =grade,
            enrollment_date=enrollment_date,
        )
        return redirect('studentList')
    return render(request, 'addStudent.html')
def studentList(request):
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            studentData = studentModel.objects.all()
        else:
            teacher = teacherModel.objects.get(user=request.user)
            studentData = studentModel.objects.filter(teacher=teacher)
    else:
        studentData = studentModel.objects.none()

    return render(request, 'studentList.html', {'student': studentData})

def editStudent(request,id):
    studentData = studentModel.objects.get(id=id)
    if request.method == 'POST':
        studentData.first_name = request.POST.get('first_name')
        studentData.last_name = request.POST.get('last_name')
        studentData.age = request.POST.get('age')
        studentData.grade = request.POST.get('grade')
        studentData.enrollment_date = request.POST.get('enrollment_date')
        studentData.teacher = teacherModel.objects.get(user=request.user)

        studentData.save()
        return redirect('studentList')
    studentData = studentModel.objects.get(id=id)
    return render(request, 'editStudent.html', {'student': studentData})
def viewStudent(request,id):
    studentData = studentModel.objects.get(id=id)
    return render(request, 'viewStudent.html', {'student': studentData})
def deleteStudent(request,id):
    studentData = studentModel.objects.get(id=id).delete()
    return redirect('studentList')
