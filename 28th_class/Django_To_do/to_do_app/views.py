from django.shortcuts import render,redirect
from to_do_app.models import *
from django.contrib.auth import authenticate,login,logout,hashers,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city_name = request.POST.get('city_name')
        bio = request.POST.get('bio')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            customUserModel.objects.create_user(
                image=image,
                username=username,
                full_name=full_name,
                phone=phone,
                email=email,
                address=address,
                city_name=city_name,
                bio=bio,
                password=confirm_password,
            )
            return redirect('loginPage')

    return render(request, 'signupPage.html')
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return redirect('passwordWrong')
    return render(request, 'loginPage.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')


@login_required
def home(request):
    total = itemModel.objects.filter(user = request.user )
    in_progress_items = itemModel.objects.filter(user = request.user, status='in_progress' )
    pending_items = itemModel.objects.filter(user = request.user, status='pending' )
    completed_items = itemModel.objects.filter(user = request.user, status='completed' )
    return render(request, 'home.html', {'total':total, 'in_progress_items':in_progress_items, 'pending_items': pending_items, 'completed_items': completed_items})

@login_required
def itemList(request):
    itemData = itemModel.objects.filter(user = request.user )
    return render(request, 'itemList.html', {'items': itemData})


@login_required
def addItem(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')

        itemModel.objects.create(
            user = request.user,
            title=title,
            description=description,
            status=status,
        )
        return redirect('itemList')
    return render(request, 'addItem.html')

@login_required
def editItem(request,id):
    itemData = itemModel.objects.get(id=id)
    if request.method == 'POST':
        itemData.title = request.POST.get('title')
        itemData.description = request.POST.get('description')
        itemData.status = request.POST.get('status')
        itemData.save()
        return redirect('itemList')

    return render(request, 'editItem.html', {'items':itemData})

@login_required
def viewItem(request,id):
    itemData = itemModel.objects.get(id=id)
    return render(request, 'viewItem.html', {'items':itemData})

@login_required
def deleteItem(request,id):
    itemModel.objects.get(id=id).delete()
    return redirect('itemList')


@login_required
def passwordNotMatched(request):
    return render(request, 'passwordNotMatched.html')

@login_required
def passwordWrong(request):
    return render(request, 'passwordWrong.html')


def changePassword(request):
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