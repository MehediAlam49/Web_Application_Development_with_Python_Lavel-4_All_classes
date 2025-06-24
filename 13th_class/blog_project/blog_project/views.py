from django.shortcuts import render, redirect
from blogs.models import *

def home(request):
    return render(request, 'home.html')
def allBlogs(request):
    blogData = contentModel.objects.all()
    return render(request, 'allBlogs.html', {'blog': blogData})
def allUser(request):
    userData = userModel.objects.all()
    return render(request, 'allUser.html', {'user': userData})
def createUser(request):
    return render(request, 'createUser.html')
def createBlogs(request):
    if request.method == 'POST':
        blog = contentModel(
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            email = request.POST.get('email'),
            description = request.POST.get('description'),
        )
        blog.save()
        return redirect('allBlogs')
    return render(request, 'createBlogs.html')

def deleteBlogs(request,id):
    blogData = contentModel.objects.get(id=id).delete()
    return redirect('allBlogs')