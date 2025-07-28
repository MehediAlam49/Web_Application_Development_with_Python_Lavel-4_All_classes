from django.shortcuts import render, redirect
from myApp.models import *

# Create your views here.
def home(request):
    infoData = infoModel.objects.all()
    return render(request, 'home.html', {'info': infoData})

def create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        about = request.POST.get('about')
        phone = request.POST.get('phone')

        infoData = infoModel(
            image = image,
            name = name,
            about = about,
            phone = phone,
        )
        infoData.save()
        return redirect('home')
    return render(request, 'create.html')

def view(request,id):
    infoData = infoModel.objects.get(id=id)
    return render(request, 'read.html', {'info': infoData})
    
def update(request,id):
    infoData = infoModel.objects.get(id=id)
    if request.method == 'POST':
        infoData.name = request.POST.get('name')
        infoData.about = request.POST.get('about')
        infoData.phone = request.POST.get('phone')

        picture = request.FILES.get('image')
        if picture is not None:
            infoData.image = picture
        infoData.save()
        return redirect('home')
    return render(request, 'update.html', {'info': infoData})
def delete(request,id):
    info = infoModel.objects.get(id=id).delete()
    return redirect('home')
