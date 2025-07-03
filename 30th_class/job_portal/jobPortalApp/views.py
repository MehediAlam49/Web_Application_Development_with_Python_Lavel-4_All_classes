from django.shortcuts import render,redirect,HttpResponse
from jobPortalApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            customUserModel.objects.create_user(
                full_name=full_name,
                username=username,
                email=email,
                bio = bio,
                phone=phone,
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
    return render(request, 'loginPage.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def home(request):
    return render(request, 'home.html')

def addJob(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        logo = request.FILES.get('logo')
        job_type = request.POST.get('job_type')

        jobModel.objects.create(
            created_by = request.user,
            title=title,
            description=description,
            logo=logo,
            job_type=job_type,
        )
        return redirect('jobFeed')

    return render(request, 'addJob.html')
def jobFeed(request):
    jobData = jobModel.objects.filter(created_by=request.user)
    return render(request, 'jobFeed.html', {'job':jobData})

def editJob(request, id):
    jobData = jobModel.objects.get(id=id)
    if request.method == 'POST':
        jobData.title = request.POST.get('title')
        jobData.description = request.POST.get('description')
        jobData.job_type = request.POST.get('job_type')

        picture = request.FILES.get('logo')
        if picture is not None:
            jobData.logo = picture
            jobData.save()
        
        return redirect('jobFeed')

    return render(request, 'editJob.html', {'job':jobData})
def deleteJob(request, id):
    jobModel.objects.get(id=id).delete()
    return redirect('jobFeed')