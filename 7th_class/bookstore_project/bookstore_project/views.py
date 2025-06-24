from django.shortcuts import render, redirect
from store.models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')
def books(request):
    bookData = bookModel.objects.all()
    context = {
        'bookData': bookData,
    }
    return render(request, 'books.html', context)
def user(request):
    userData = userModel.objects.all()
    context = {
        'userData': userData,
    }
    return render(request, 'user.html', context)
def addStudent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        student = studentModel(name=name, email=email, address=address, phone=phone)
        student.save()
        return redirect('studentList')
    return render(request, 'addStudent.html')
def studentList(request):
    context = {
        'studentData':studentModel.objects.all()
    }
    return render(request,'studentList.html',context)