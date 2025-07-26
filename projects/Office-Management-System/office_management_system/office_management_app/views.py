from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from office_management_app.models import *
from django.shortcuts import get_object_or_404

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            CustomUserModel.objects.create_user(
                username=username,
                email=email,
                user_type=user_type,
                password=confirm_password,
            )
            return redirect('loginPage')
    return render(request, 'registerPage.html')
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'loginPage.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def home(request):
    return render(request, 'home.html')
def profile(request):
    employerData = EmployeeManagementModel.objects.get(user=request.user)
    return render(request, 'profile.html',{'employerData':employerData})


def addDepartment(request):
    if request.method == 'POST':
        department_name = request.POST.get('department_name')
        description = request.POST.get('description')

        DepartmentModel.objects.create(
            department_name=department_name,
            description=description
        )
        return redirect('departmentList')
    return render(request, 'addDepartment.html')

def departmentList(request):
    departmentData = DepartmentModel.objects.all()
    return render(request, 'departmentList.html',{'departmentData':departmentData})


def addEmployer(request):
    departmentData = DepartmentModel.objects.all()
    if request.method == 'POST':
        department_id = request.POST.get('department')
        department = get_object_or_404(DepartmentModel, id=department_id)

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        position = request.POST.get('position')
        join_date = request.POST.get('join_date')
        profile = request.FILES.get('profile')

        user = CustomUserModel.objects.create_user(
            username=email,
            password=phone,
            user_type = 'Employee',
        )
        
        if user:
            EmployeeManagementModel.objects.create(
                department= department,
                full_name=full_name,
                email=email,
                phone=phone,
                position=position,
                join_date=join_date,
                profile=profile,
            )
        return redirect('employerList')
    return render(request, 'addEmployer.html',{'departmentData':departmentData})

def employerList(request):
    employerData = EmployeeManagementModel.objects.all()
    return render(request, 'employerList.html',{'employerData':employerData})

def addLeave(request):
    employees= EmployeeManagementModel.objects.all()
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        employee = get_object_or_404(EmployeeManagementModel, id=employee_id)

        leave_type = request.POST.get('leave_type')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        reason = request.POST.get('reason')

        LeaveModel.objects.create(
            employee=employee,
            leave_type=leave_type,
            from_date=from_date,
            to_date=to_date,
            reason=reason,
            status='Pending'
        )
        return redirect('leaveList')
    return render(request, 'addLeave.html',{'employees':employees})

def leaveList(request):
    leaveData = LeaveModel.objects.all()
    return render(request, 'leaveList.html',{'leaveData':leaveData})