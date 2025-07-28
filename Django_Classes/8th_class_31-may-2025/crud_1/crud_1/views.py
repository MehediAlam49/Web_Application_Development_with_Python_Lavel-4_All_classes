from django.shortcuts import render, redirect
from library.models import *

def home(request):
    return render(request, 'home.html')
def book(request):
    context = {'bookData': bookModel.objects.all()}
    return render(request, 'book.html',context)
def studentList(request):
    context = {'studentData': studentModel.objects.all()}
    return render(request, 'studentList.html',context)
def addBook(request):
    if request.method == 'POST':
        book = bookModel(
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            date = request.POST.get('date'),
            price = request.POST.get('price'),
            stock = request.POST.get('stock'),
        )
        book.save()
        return redirect("book")
    return render(request, 'addBook.html')
def addStudent(request):
    if request.method == 'POST':
        student = studentModel(
        name = request.POST.get('name'),
        department = request.POST.get('department'),
        semester = request.POST.get('semester'),
        date = request.POST.get('date'),
        )
        student.save()
        return redirect('studentList')
    return render(request, 'addStudent.html')