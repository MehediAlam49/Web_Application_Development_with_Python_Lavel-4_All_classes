from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from user_auth_app.models import *
from employer_app.models import *
from candidate_app.models import *

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user_type = request.POST.get('user_type')
        

        if user_type == 'Admin':
            CustomUserModel.objects.create_user(
                username=username, 
                email=email, 
                user_type = 'Admin',
                phone=phone,
                password=phone,
            )

        else:
            PendingAccountModel.objects.create(
                username=username, 
                email=email, 
                user_type = user_type,
                phone=phone,
                pending_status='Pending'
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
            messages.error(request, 'Invalid username or password.')
            return redirect('loginPage')

    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def homePage(request):
    profile_list = CustomUserModel.objects.all()
    return render(request, 'home.html', {'profile_list':profile_list})

def profileInfo(request):
    return render(request, 'profileInfo.html')




def pendingListPage(request):
    pendingAccount = PendingAccountModel.objects.all()
    return render(request, 'pendingPage.html',{'pendingAccount':pendingAccount})

def acceptPendingaccount(request,id):
    pendingAccount = PendingAccountModel.objects.get(id=id)

    if pendingAccount:
        userData = CustomUserModel.objects.create_user(
            username=pendingAccount.username,
            email=pendingAccount.email,
            password=pendingAccount.phone,
            user_type = pendingAccount.user_type,
            phone=pendingAccount.phone,
        )
        if userData:
            if pendingAccount.user_type == 'Employer':
                EmployerProfileModel.objects.create(
                    employer_user = userData,
                    email = pendingAccount.email,
                    phone = pendingAccount.phone,

                )
            elif pendingAccount.user_type == 'Candidate':
                CandidateProfileModel.objects.create(
                    candidate_user = userData,
                    email = pendingAccount.email,
                    phone = pendingAccount.phone,
                )
        pendingAccount.delete()
    return redirect('pendingListPage')


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