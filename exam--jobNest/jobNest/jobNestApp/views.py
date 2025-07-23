from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib import messages
from jobNestApp.models import *
from jobNestApp.forms import JobModelForm

# Create your views here.

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            CustomUserModel.objects.create_user(
                username=username, 
                email=email, 
                user_type = user_type,
                phone=phone,
                password=confirm_password,
            )
            return redirect(loginPage)
    return render(request, 'register.html')





def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            return redirect('loginPage')

    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def profileInfo(request):
    profile_list = CustomUserModel.objects.all()
    return render(request, 'profileInfo.html', {'profile_list':profile_list})

# def editProfile(request,id):
    
#     profile_data = CustomUserModel.objects.get(id=id)

#     if request.method == 'POST':
#         profile_data.username=request.POST.get('username')
#         profile_data.email=request.POST.get('email')
#         profile_data.phone=request.POST.get('phone')

#         return redirect('profileInfo')
    
#     context={
#         'profile_data':profile_data,
#     }
#     return render(request, 'editProfile.html',context)



def homePage(request):
    profile_list = CustomUserModel.objects.all()
    return render(request, 'home.html', {'profile_list':profile_list})

def changePasswordPage(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        user = request.user

        if not user.check_password(old_password):
            messages.error(request, 'Current password is incorrect.')
            return render(request, 'changePassword.html')

        if new_password1 != new_password2:
            messages.error(request, 'New passwords do not match.')
            return render(request, 'changePassword.html')


        # Set new password
        user.set_password(new_password1)
        user.save()

        update_session_auth_hash(request, user)

        messages.success(request, 'Your password has been updated successfully.')
        return redirect('profileInfo') 
    return render(request, 'changePassword.html')


def addJob(request):
    if request.method == 'POST':
        job_form = JobModelForm(request.POST)
        if job_form.is_valid():
            job_form.save()
            return redirect('jobListPage')
    else:
        job_form = JobModelForm()
    return render(request, 'addJob.html', {'job_form': job_form})
