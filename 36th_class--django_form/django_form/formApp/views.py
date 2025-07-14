from django.shortcuts import render, redirect
from formApp.form import *
from formApp.models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def userInfoView(request):
    form = UserInfoForm(request.POST, request.FILES)
    if form.is_valid():
        full_name = form.cleaned_data['full_name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        address = form.cleaned_data['address']

        UserInfoModel.objects.create(
            full_name=full_name,
            phone=phone,
            email=email,
            address=address,
        )
        return redirect('home')
    

def basicInfoView(request):
    if request.method == 'POST':
        basic_info = BasicInfoForm(request.POST, request.FILES)
        if basic_info.is_valid():
            basic_info.save()
            return redirect('home')
    else:
        basic_info= BasicInfoForm()

    context ={
        'basic_info':basic_info
    }
    return render(request, 'basicInfoView.html',context)