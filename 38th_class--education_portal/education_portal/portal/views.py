from django.shortcuts import render,redirect
from portal.models import *
from portal.form import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=confirm_password,
                user_type = 'Admin',
            )
            user.save()
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

def home(request):
    return render(request, 'home.html')

def addTeacher(request):
    if request.method == 'POST':
        teacher_info = TeacherForm(request.POST)
        if teacher_info.is_valid():
            teacher_info.save()
            return redirect('teacher_list')
    else:
        teacher_info= TeacherForm()
        
    context ={
        'teacher_info':teacher_info
    }
    
    return render(request, 'addTeacher.html', context)

# def add_teacher(request):
#     if request.method == 'POST':
#         form = TeacherForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher_list')  # Replace with your list view name
#     else:
#         form = TeacherForm()

#     return render(request, 'addTeacher.html', {'teacher_info': form})

def teacher_list(request):
    teacher_info = TeacherModel.objects.all()
    return render(request, 'teacher_list.html', {'teacher_info':teacher_info})


def addStudent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        degree_name = request.POST.get('degree_name')
        grade = request.POST.get('grade')
        passing_year = request.POST.get('passing_year')
        
        
        student_info = StudentBasicInfoModel.objects.create(
            name=name,
            email=email,
            address=address,
        )
        if student_info:
            EducationInfoModel.objects.create(
                student = student_info,
                degree_name=degree_name,
                grade=grade,
                passing_year=passing_year,

            )
        return redirect('studentList')
    return render(request, 'addStudent.html')

def studentList(request):
    studentData = EducationInfoModel.objects.all()
    return render(request, 'studentList.html', {'student': studentData})
