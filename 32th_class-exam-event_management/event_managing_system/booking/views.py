from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash,hashers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            EventUserModel.objects.create_user(
                profile_image=profile_image,
                username=username,
                full_name=full_name,
                email=email,
                phone_number=phone_number,
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
    return render(request,'loginPage.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request,'profile.html')

def addBooking(request):
    if request.method == 'POST':
        event_title = request.POST.get('event_title')
        event_type = request.POST.get('event_type')
        event_description = request.POST.get('event_description')
        event_date = request.POST.get('event_date')
        status = request.POST.get('status')
        location = request.POST.get('location')

        EventBookingModel.objects.create(
            created_by = request.user,
            event_title=event_title,
            event_type=event_type,
            event_description=event_description,
            event_date=event_date,
            status=status,
            location=location,
        )
        return redirect('myBooking')
    return render(request,'addBooking.html')
def myBooking(request):
    bookData = EventBookingModel.objects.filter(created_by = request.user)
    return render(request,'myBooking.html', {'book': bookData})
def editBooking(request,id):
    bookData = EventBookingModel.objects.get(id=id)
    if request.method == 'POST':
        bookData.event_title = request.POST.get('event_title')
        bookData.event_type = request.POST.get('event_type')
        bookData.event_description = request.POST.get('event_description')
        bookData.event_date = request.POST.get('event_date')
        bookData.status = request.POST.get('status')
        bookData.location = request.POST.get('location')

        bookData.save()
        return redirect('myBooking')
    return render(request,'editBooking.html', {'book': bookData})
def viewBooking(request,id):
    bookData = EventBookingModel.objects.get(id=id)
    return render(request,'viewBooking.html', {'book': bookData})
def deleteBooking(request,id):
    bookData = EventBookingModel.objects.get(id=id).delete()
    return redirect('myBooking')


def statusChange(request, id):
    bookData = EventBookingModel.objects.get(id=id)
    if bookData.status == 'NotStarted':
        bookData.status = 'InProgress'
    elif bookData.status == 'InProgress':
        bookData.status = 'Completed'
    bookData.save()
    return redirect('myBooking')



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